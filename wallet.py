import hashlib
import requests

def create_wallet():
    private_key = hashlib.sha256(b'some_random_private_key').hexdigest()
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    return private_key, public_key

def send_transaction(sender, receiver, amount, node_url):
    transaction = {
        'sender': sender,
        'receiver': receiver,
        'amount': amount
    }
    response = requests.post(f'{node_url}/transactions/new', json=transaction)
    return response.json()

if __name__ == '__main__':
    private_key, public_key = create_wallet()
    print(f'Wallet created!\nPublic Key: {public_key}\nPrivate Key: {private_key}')

    # Optional: Send a sample transaction
    node_url = 'http://127.0.0.1:5000'
    response = send_transaction(public_key, 'Bob', 100, node_url)
    print(response)
