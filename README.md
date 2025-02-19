# Peer-to-Peer Messaging Application

## Overview
The Peer-to-Peer Messaging Application is a Python-based project designed for simple and direct communication between multiple peers. Using socket programming and multithreading, the application facilitates real-time message exchange over a network, allowing users to connect, send, and receive messages with ease.

## Features
- **Peer Connection Management**
  - Maintains an active list of connected peers using a global dictionary.
  - Supports dynamic updating of peer information when connection messages are received.
- **Multi-threaded Operation**
  - Uses separate threads for handling incoming connections and client messages to ensure smooth communication.
- **Local IP Detection**
  - Automatically determines and displays your local IP address for external sharing with peers.
- **Interactive Command-Line Interface**
  - Provides a menu-driven interface to send messages, query active peers, and connect to new peers.
- **Mandatory Messaging**
  - Automatically sends predefined mandatory messages to two specified IP addresses upon startup.
- **Customizable Identification**
  - Users set a team name which is appended to every outgoing message, making communication clear and organized.

## Prerequisites
- **Python Version:** Python 3.x is required.
- **Libraries:** Uses Python's standard libraries (`socket`, `threading`, `sys`, and `time`) – no external dependencies are necessary.

## Installation
1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>

### Flask Web Interface
- **Dynamic Chat UI:**  
  A sleek, browser-based interface that displays active peers, chat history, and provides interactive forms for sending messages.
- **Real-Time Updates:**  
  Periodically updates both chat messages and the active peer list.
  ![Chat Application Screenshot](Images/Screenshot%202025-02-19%20154937.png)
  ![Chat Application Screenshot](/Images/Screenshot%202025-02-19%20162514.png).


## Prerequisites
- Python 3.6 or higher
- Flask (for the web interface)
- Basic knowledge of networking and Python programming

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/p2p-flask-chat.git
cd p2p-flask-chat
