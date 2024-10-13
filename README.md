# Crypcur

MyCoin: A Simple Cryptocurrency on Blockchain
This repository contains a complete cryptocurrency project built with Python. The goal is to demonstrate core concepts of blockchain and cryptocurrency creation, including block mining, transaction handling, and blockchain validation. This project is designed to be simple but provides a solid foundation for further expansion.

Table of Contents
Project Overview
Features
Getting Started
How to Run
API Endpoints
Code Explanation
Enhancements
License
Project Overview
This project showcases a basic cryptocurrency called MyCoin running on a custom blockchain. It covers all the necessary components:

Blockchain structure
Block mining with Proof of Work
Transaction management
Node communication through Flask APIs
It is designed to simulate a decentralized currency where nodes can mine blocks, verify transactions, and maintain consensus over the chain's integrity.

Features
Blockchain Management: Add and validate new blocks with transactions.
Proof of Work Mining: Implements a simple mining algorithm for block creation.
Transactions: Create transactions with wallets.
Flask-based Node: Each node serves blockchain data through a REST API.
Chain Validation: Ensures the blockchain remains tamper-proof.
Getting Started
Prerequisites
Ensure you have the following installed on your system:

Python 3.x
pip (Python package installer)
Installing Dependencies
Clone the repository and install the required packages:

bash
Copy code
git clone https://github.com/your-username/mycoin.git
cd mycoin
pip install -r requirements.txt
How to Run
Start the Node Server:
Run the node server to handle transactions and blocks.

bash
Copy code
python node.py
Create a Wallet (Optional):
Generate a wallet to send transactions.

bash
Copy code
python wallet.py
Test the API using cURL or Postman:
Use the API to add transactions and mine blocks (see API Endpoints).

API Endpoints
Mine a Block
Mines a new block and adds it to the blockchain.

http
Copy code
GET /mine
Response:

json
Copy code
{
  "message": "Block mined successfully!",
  "block": { ... }
}
Create a New Transaction
Creates a transaction to be added to the next mined block.

http
Copy code
POST /transactions/new
Content-Type: application/json
{
  "sender": "Alice",
  "receiver": "Bob",
  "amount": 50
}
Response:

json
Copy code
{
  "message": "Transaction will be added to Block 2"
}
Get the Full Blockchain
Fetches the entire blockchain with all blocks.

http
Copy code
GET /chain
Response:

json
Copy code
{
  "chain": [ ... ],
  "length": 2
}
Code Explanation
1. Blockchain Class (blockchain.py)
The Blockchain class manages the blockchain. Key methods include:

create_block: Creates a new block with transactions.
proof_of_work: Implements the Proof of Work algorithm to mine blocks.
is_chain_valid: Validates the entire blockchain.
2. Node Setup (node.py)
The Flask server acts as a node. It exposes APIs to mine blocks, add transactions, and retrieve the blockchain.

3. Wallet (wallet.py)
This file contains logic to generate a wallet with public and private keys. It also provides functions to send transactions to the node.

4. Utility Functions (utils.py)
Contains helper functions like hash_data to hash strings using SHA-256.

Enhancements
This project provides a basic cryptocurrency but can be extended with:

Peer-to-Peer Network: Set up multiple nodes communicating with each other.
RSA Cryptography: Secure transactions with public/private key pairs.
Smart Contracts: Introduce contract logic on the blockchain.
Frontend UI: Build a simple web interface to interact with the node.
Advanced Mining Algorithm: Implement more complex Proof of Work or switch to Proof of Stake.
License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as you wish.

Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

Acknowledgments
Special thanks to the open-source blockchain and cryptocurrency community for inspiration.
