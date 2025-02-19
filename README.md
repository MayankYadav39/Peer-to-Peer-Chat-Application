# Peer-to-Peer Chat Application

## Overview
This Peer-to-Peer Chat Application is a Python-based project that enables direct communication between multiple users without the need for a centralized server. It leverages socket programming and multithreading to allow real-time message exchange among connected peers.

## Features
- **Peer Connection Management**
  - Maintains an active list of connected peers.
  - Dynamically updates connection details when peers send connection messages.
- **Multi-threaded Operation**
  - Uses separate threads for handling incoming connections and processing client messages.
- **Local IP Detection**
  - Automatically detects and displays your local IP address for sharing with peers.
- **Interactive Command-Line Interface**
  - Menu-driven interface for sending messages, querying active peers, and connecting to new peers.
- **Mandatory Messaging**
  - Automatically sends preset mandatory messages to specific IP addresses upon startup.
- **Customizable Identification**
  - Allows users to set a team name that prefixes all outgoing messages.

## Prerequisites
- **Python Version:** Python 3.x is required.
- **Libraries:** Uses standard Python libraries such as `socket`, `threading`, `sys`, and `time`.

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/MayankYadav39/Peer-to-Peer-Chat-Application.git
   cd Peer-to-Peer-Chat-Application


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
