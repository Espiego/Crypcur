

CrypCur: A Simple Cryptocurrency on Blockchain
This repository contains a complete cryptocurrency project named CrypCur, built with Python. 

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
CrypCur is a basic cryptocurrency running on a custom blockchain. It allows nodes to mine blocks, verify transactions, and maintain consensus over the integrity of the blockchain. It showcases all the necessary components of a cryptocurrency system:

Blockchain Structure
Proof of Work Mining Algorithm
Transaction Management
Node Communication via Flask APIs
Blockchain Validation for Tamper-proofing
Features
Blockchain Management: Add and validate new blocks with transactions.
Proof of Work Mining: Implements a basic mining algorithm for block creation.
Transaction System: Create transactions between wallets.
RESTful APIs: Flask-based APIs to interact with the blockchain.
Blockchain Validation: Ensures the chain remains tamper-proof and consistent.
Getting Started
Prerequisites
Ensure you have the following installed on your machine:

- Python 3.x
- pip (Python package installer)
- Installing Dependencies
- Clone the repository and install the required packages:



Enhancements
CrypCur is a basic implementation of cryptocurrency. You can extend it with the following features:

-Peer-to-Peer Network: Enable communication between multiple nodes.
-RSA Cryptography: Secure transactions using public and private key pairs.
-Smart Contracts: Introduce programmable contracts on the blockchain.
-Web UI: Build a frontend interface to make the project more interactive.
-Advanced Mining Algorithm: Switch from Proof of Work to Proof of Stake for better efficiency.


Contributing
Pull requests are welcome! If you wish to make major changes, please open an issue to discuss your ideas before submitting.

Acknowledgments
Special thanks to the open-source blockchain and cryptocurrency community for providing resources and inspiration for this project.

Run Instructions
Install dependencies:


pip install -r requirements.txt
Run the Flask node server:

python node.py
Create a wallet and generate a public/private key pair:


python wallet.py
Test the APIs:

Use cURL or Postman to interact with the CrypCur blockchain:

Mine a block:


curl http://127.0.0.1:5000/mine
Add a transaction:


curl -X POST http://127.0.0.1:5000/transactions/new \
-H "Content-Type: application/json" \
-d '{"sender": "Alice", "receiver": "Bob", "amount": 50}'
Retrieve the blockchain:


curl http://127.0.0.1:5000/chain
