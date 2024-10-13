import hashlib
import time
import json

class Blockchain:
    def __init__(self):
        self.chain = []  # Blockchain to store blocks
        self.pending_transactions = []  # Transactions waiting to be added to a block
        self.create_block(proof=1, previous_hash='0')  # Genesis block

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time.time(),
            'transactions': self.pending_transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.pending_transactions = []  # Clear pending transactions
        self.chain.append(block)
        return block

    def get_last_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        while not self.valid_proof(new_proof, previous_proof):
            new_proof += 1
        return new_proof

    def valid_proof(self, proof, previous_proof):
        guess = f'{proof}{previous_proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"  # Simple difficulty

    def add_transaction(self, sender, receiver, amount):
        self.pending_transactions.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return self.get_last_block()['index'] + 1  # Block index

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]
            if current_block['previous_hash'] != self.hash_block(previous_block):
                return False
            if not self.valid_proof(current_block['proof'], previous_block['proof']):
                return False
        return True

    @staticmethod
    def hash_block(block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
