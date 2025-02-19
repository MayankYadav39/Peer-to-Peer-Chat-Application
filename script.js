// Mock function to get local IP (Replace dynamically if needed)
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("local-ip").innerText = "192.168.1.100"; // Example IP
});

// Handling Send Message Button
document.getElementById("send-message-btn").addEventListener("click", function() {
    let targetIP = document.getElementById("target-ip").value;
    let targetPort = document.getElementById("target-port").value;
    let message = document.getElementById("message").value;

    if (targetIP === "" || targetPort === "" || message === "") {
        alert("Please fill in all fields!");
        return;
    }

    let chatHistory = document.getElementById("chat-history");
    let newMessage = document.createElement("p");
    newMessage.innerHTML = `<strong>You:</strong> ${message}`;
    chatHistory.appendChild(newMessage);
    
    // Clear input fields
    document.getElementById("message").value = "";
});

// Handling Peer Connection
document.getElementById("connect-btn").addEventListener("click", function() {
    alert("Connecting to peer...");
});

// Handling Active Peers Display
document.getElementById("active-peers-btn").addEventListener("click", function() {
    alert("Fetching active peers...");
});
