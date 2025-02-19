import socket
import threading
import sys
import time
from flask import Flask, request, jsonify, render_template, redirect, url_for

###############################################
# Global variables and locks for peer networking
###############################################

# Active peers dictionary: key=(peer_ip, peer_listen_port), value=socket object.
active_peers = {}
peers_lock = threading.Lock()

# Event to signal shutdown.
shutdown_event = threading.Event()

# Global variables for our listening port and team name.
my_listen_port = None
team_name = None

# Chat history list to store messages (each is a dict with sender, message, timestamp)
chat_history = []
chat_lock = threading.Lock()

def add_chat_message(sender, message):
    """Thread-safe addition of a chat message."""
    with chat_lock:
        chat_history.append({
            'sender': sender,
            'message': message,
            'timestamp': time.strftime('%H:%M:%S')
        })

def get_local_ip():
    """
    Determines the local IP address used for outgoing connections.
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 80))
        local_ip = s.getsockname()[0]
    except Exception:
        local_ip = '127.0.0.1'
    finally:
        s.close()
    return local_ip

###############################################
# Peer-to-peer socket functions
###############################################

def handle_client(conn, addr):
    """
    Handles messages from a connected peer.
    If the peer sends a "CONNECT:<listening_port>" message, we update our record.
    Also, non-control messages are added to the chat history.
    """
    global active_peers
    current_peer = addr
    try:
        while not shutdown_event.is_set():
            data = conn.recv(1024)
            if not data:
                print(f"[INFO] Connection closed by {current_peer[0]}:{current_peer[1]}")
                break
            message = data.decode().strip()
            if not message:
                continue

            # Handle a connection update message.
            if message.startswith("CONNECT:"):
                try:
                    sender_listen_port = int(message.split(":", 1)[1])
                    new_peer = (current_peer[0], sender_listen_port)
                except ValueError:
                    print(f"[ERROR] Invalid CONNECT message from {current_peer}")
                    continue

                with peers_lock:
                    active_peers.pop(current_peer, None)
                    if new_peer in active_peers:
                        try:
                            active_peers[new_peer].close()
                        except Exception:
                            pass
                    active_peers[new_peer] = conn
                current_peer = new_peer
                print(f"[INFO] Updated connection info for peer {new_peer[0]}:{new_peer[1]}")
                continue

            # If a peer sends "exit", then disconnect.
            if message.lower() == "exit":
                print(f"[INFO] {current_peer[0]}:{current_peer[1]} sent exit. Disconnecting.")
                break

            # Log the received message.
            print(f"[Message from {current_peer[0]}:{current_peer[1]}]: {message}")
            add_chat_message(f"{current_peer[0]}:{current_peer[1]}", message)

    except Exception as e:
        print(f"[ERROR] Exception with peer {current_peer[0]}:{current_peer[1]}: {e}")
    finally:
        with peers_lock:
            active_peers.pop(current_peer, None)
        conn.close()


def server_thread(listen_socket):
    """
    Accept incoming connections and spawn a dedicated thread for each.
    """
    while not shutdown_event.is_set():
        try:
            listen_socket.settimeout(1.0)
            conn, addr = listen_socket.accept()
        except socket.timeout:
            continue
        except Exception as e:
            if not shutdown_event.is_set():
                print(f"[ERROR] Accept failed: {e}")
            break

        print(f"[INFO] Accepted connection from {addr[0]}:{addr[1]}")
        with peers_lock:
            active_peers[addr] = conn
        client_thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
        client_thread.start()


def send_message(target_ip, target_port, message):
    """
    Sends a message to the target peer.
    If no active connection exists, creates a new connection.
    """
    target = (target_ip, target_port)
    with peers_lock:
        sock = active_peers.get(target)

    if sock is None:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)  # 10-second timeout for connecting.
            print(f"[DEBUG] Attempting to connect to {target_ip}:{target_port}")
            sock.connect(target)
            sock.settimeout(None)
            with peers_lock:
                active_peers[sock.getpeername()] = sock
            client_thread = threading.Thread(target=handle_client, args=(sock, sock.getpeername()), daemon=True)
            client_thread.start()
        except Exception as e:
            print(f"[ERROR] Could not connect to {target_ip}:{target_port} - {e}")
            return

    try:
        sock.sendall(message.encode())
        print(f"[INFO] Message sent to {target_ip}:{target_port}")
        if message.lower() == "exit":
            with peers_lock:
                active_peers.pop(target, None)
            sock.close()
    except Exception as e:
        print(f"[ERROR] Failed to send message: {e}")
        with peers_lock:
            active_peers.pop(target, None)
        sock.close()


def connect_to_peer(target_ip, target_port):
    """
    Connects to a peer by sending a connection message that includes our listening port.
    """
    global my_listen_port
    target = (target_ip, target_port)
    with peers_lock:
        sock = active_peers.get(target)

    if sock is None:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10)
            print(f"[DEBUG] Attempting to connect to {target_ip}:{target_port}")
            sock.connect(target)
            sock.settimeout(None)
            with peers_lock:
                active_peers[sock.getpeername()] = sock
            client_thread = threading.Thread(target=handle_client, args=(sock, sock.getpeername()), daemon=True)
            client_thread.start()
        except Exception as e:
            print(f"[ERROR] Could not connect to {target_ip}:{target_port} - {e}")
            return

    connect_msg = f"CONNECT:{my_listen_port}"
    try:
        sock.sendall(connect_msg.encode())
        print(f"[INFO] Sent connection message to {target_ip}:{target_port}")
    except Exception as e:
        print(f"[ERROR] Failed to send connection message: {e}")
        with peers_lock:
            active_peers.pop(target, None)
        sock.close()


def send_mandatory_messages():
    """
    Sends a mandatory message to two specified IP/port pairs.
    """
    mandatory_peers = [
        ("10.206.4.122", 1255),
        ("10.206.5.228", 6555)
    ]
    for ip, port in mandatory_peers:
        print(f"[INFO] Attempting to send mandatory message to {ip}:{port}")
        send_message(ip, port, "Mandatory message: Hello from our peer!")


###############################################
# Flask application and routes
###############################################

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send", methods=["POST"])
def send():
    target = request.form.get("target", "all")
    message = request.form.get("message", "").strip()
    if not message:
        return redirect(url_for('index'))
    
    # Add local message to chat history.
    add_chat_message(team_name, message)
    
    # Send the message: if "all", iterate over active peers.
    if target == "all":
        with peers_lock:
            peers = list(active_peers.keys())
        for peer in peers:
            send_message(peer[0], peer[1], f"{team_name}: {message}")
    else:
        # Expect target in the form "ip:port"
        try:
            ip, port_str = target.split(":")
            port = int(port_str)
            send_message(ip, port, f"{team_name}: {message}")
        except Exception as e:
            print(f"[ERROR] Invalid target: {target} - {e}")
    return redirect(url_for('index'))

@app.route("/connect", methods=["POST"])
def connect():
    peer_ip = request.form.get("peer_ip", "").strip()
    try:
        peer_port = int(request.form.get("peer_port", "").strip())
    except ValueError:
        return redirect(url_for('index'))
    
    threading.Thread(target=connect_to_peer, args=(peer_ip, peer_port), daemon=True).start()
    return redirect(url_for('index'))

@app.route("/updates", methods=["GET"])
def updates():
    # Return JSON with current chat history and active peers.
    with chat_lock:
        chat = list(chat_history)
    with peers_lock:
        peers = [f"{ip}:{port}" for (ip, port) in active_peers.keys()]
    return jsonify({"chat_history": chat, "active_peers": peers})

def main():
    global my_listen_port, team_name

    # Get team name and listening port from the user.
    team_name = input("Enter your team name: ").strip()
    try:
        my_listen_port = int(input("Enter your port number (for incoming peer connections): ").strip())
    except ValueError:
        print("[ERROR] Invalid port number. Exiting.")
        sys.exit(1)

    local_ip = get_local_ip()
    print(f"[INFO] Your local IP address is: {local_ip}")
    print("[INFO] Share this IP and your port with peers for connecting externally.")

    # Set up the listening socket for peer connections.
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    try:
        listen_socket.bind(("0.0.0.0", my_listen_port))
    except Exception as e:
        print(f"[ERROR] Could not bind to port {my_listen_port}: {e}")
        sys.exit(1)

    listen_socket.listen(5)
    print(f"[INFO] Peer server listening on port {my_listen_port}...")

    # Start the peer server thread.
    server = threading.Thread(target=server_thread, args=(listen_socket,), daemon=True)
    server.start()

    # Give the server thread a moment to start.
    time.sleep(2)

    # Send mandatory messages (optional).
    send_mandatory_messages()

    # Now start the Flask web interface (running on port 5000).
    try:
        app.run(host="0.0.0.0", port=5000, debug=False, use_reloader=False)
    except KeyboardInterrupt:
        print("Shutting down...")
    finally:
        shutdown_event.set()
        with peers_lock:
            for peer, sock in list(active_peers.items()):
                try:
                    sock.close()
                except Exception:
                    pass
            active_peers.clear()
        try:
            listen_socket.close()
        except Exception:
            pass
        server.join(timeout=2)
        print("Goodbye!")

if __name__ == "__main__":
    main()
