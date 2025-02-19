# Peer-to-Peer Chat Application

## Overview
This repository contains two versions of a peer-to-peer (P2P) chat system:

1. **Console-based Application** – a command-line interface (CLI) application using Python sockets and threading for real-time peer-to-peer messaging.
2. **Flask-based Web Application** – a user-friendly web interface that builds on the same P2P logic, allowing you to manage connections and exchange messages from within your browser.

Both versions enable direct communication between peers over a network without the need for a central server.

---


# Team Detail

**Team Name:** N0t_Applicable

## Team Members

1. **Mayank Yadav** – Roll No: 230002041
2. **Harshvardhan Choudhary** – Roll No: 230002027
3. **Anuj Kothari** – Roll No: 230008010
## Features

### Console-based Application
- **Peer Connection Management**
  - Maintains a list of connected peers in a global dictionary.
  - Dynamically updates peer info on receiving special connection messages.
- **Multi-threaded Operation**
  - Spawns a dedicated thread to handle each incoming peer connection, ensuring responsiveness.
- **Local IP Detection**
  - Automatically determines and displays your local IP address for peer sharing.
- **Menu-driven Interface**
  - **Send Message:** Provide peer IP/port and message.  
  - **Query Active Peers:** Lists all currently connected peers.  
  - **Connect to a Peer:** Initiates a new peer connection.
- **Mandatory Messaging**
  - Automatically sends preset messages to specific IPs/ports at startup.
- **Custom Team Name**
  - Users can set a team name to prefix all outgoing messages, making them easily identifiable.

### Flask-based Web Application
- **Real-time Browser-based Interface**
  - Enables messaging and peer management via an intuitive web UI instead of a console.
- **Dedicated Pages**
  - **Active Peers Page:** Add new peers (IP/port), view currently connected peers, and connect/disconnect.  
  - **Chat Terminal:** Send and receive messages in real time, with the option to target individual peers or broadcast to all.
- **Responsive Design**
  - Styled with a custom theme (green neon, as shown in screenshots) for a modern, visually appealing experience.
- **Peer List Synchronization**
  - Continuously updates the list of connected peers to reflect real-time status changes.
- **Message History Display**
  - Shows a running log of messages (including timestamps, sender, and content) for easy tracking of conversation flow.
- **Same Core P2P Logic**
  - Reuses the console application’s core socket and threading logic for handling connections and message passing.
     ![Chat Application Screenshot](Images/Screenshot%202025-02-19%20154937.png)
  ![Chat Application Screenshot](/Images/Screenshot%202025-02-19%20162514.png).

---

## Prerequisites
- **Python Version:** 3.x
- **Libraries:**
  - **Console Application:** Only standard Python libraries (`socket`, `threading`, `sys`, `time`).
  - **Flask Application:** Requires `Flask`. Install via:
    ```bash
    pip install flask
    ```

---

## Installation
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MayankYadav39/Peer-to-Peer-Chat-Application.git
   cd Peer-to-Peer-Chat-Application
2. **Web Application**   :
  ```bash
  cd App
  python app.py
  ```

   
