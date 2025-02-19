# Peer-To-Peer Chat Application

## Overview

This project is a versatile chat application that combines a peer-to-peer (P2P) networking module with two separate user interfaces:

1. **Terminal-Based Application:**  
   A Python script that supports terminal operations for direct TCP socket communication, featuring a menu-driven interface for sending messages, querying active peers, and connecting to peers.

2. **Flask Web Interface:**  
   A modern, browser-based chat interface that provides real-time updates, displays active peers, shows chat history, and allows users to send messages with ease.

Both implementations enable real-time messaging between peers using direct TCP socket connections and are designed with a user-friendly and minimalistic approach.

## Features

### Terminal-Based Communication
- **Direct Messaging via TCP Sockets:**  
  Enables simultaneous sending and receiving of messages.
- **Multi-threaded Handling:**  
  Supports multiple peer connections concurrently.
- **Mandatory Messaging:**  
  Automatically sends predefined messages to specific IP addresses upon startup.
- **User-Friendly CLI:**  
  A clear menu-driven interface to interact with the chat system.

### Flask Web Interface
- **Dynamic Chat UI:**  
  A sleek, browser-based interface that displays active peers, chat history, and provides interactive forms for sending messages.
- **Real-Time Updates:**  
  Periodically updates both chat messages and the active peer list.
  ![Chat Application Screenshot](Images/Screenshot%202025-02-19%20154937.png)


## Prerequisites
- Python 3.6 or higher
- Flask (for the web interface)
- Basic knowledge of networking and Python programming

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/p2p-flask-chat.git
cd p2p-flask-chat
