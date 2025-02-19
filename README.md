# Peer- To - Peer - Chat - Application

## Overview

This project is a versatile chat application that combines a peer-to-peer (P2P) networking module with a modern Flask web interface. The application enables real-time messaging between peers using direct TCP socket connections and offers a sleek web UI for managing connections, viewing active peers, and chatting.

## Features

- **Peer-to-Peer Communication:**  
  Direct messaging via TCP sockets with multi-threaded handling for multiple connections.
  
- **Flask Web Interface:**  
  A dynamic, browser-based chat interface that displays active peers, chat history, and allows users to send messages easily.
  
- **Real-Time Updates:**  
  Automatic periodic updates ensure that both chat messages and active peer lists are always current.
  
- **Mandatory Messaging:**  
  Sends predefined "mandatory" messages to specific IP addresses upon startup.
  
- **User-Friendly Design:**  
  A minimalistic, terminal-inspired UI that merges retro aesthetics with modern functionality.

## Prerequisites

- Python 3.6 or higher
- Flask (for the web interface)
- Basic knowledge of networking and Python programming

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/p2p-flask-chat.git
   cd p2p-flask-chat
