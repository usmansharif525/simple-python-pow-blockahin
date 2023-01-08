from blockchain import Blockchain, Block

# Create a new blockchain with the node ID 'node1'.
blockchain = Blockchain('node1')

# Add some transactions to the pending transactions list.
blockchain.add_transaction({
    "from": "Alice",
    "to": "Bob",
    "amount": 10
})
blockchain.add_transaction({
    "from": "Bob",
    "to": "Charlie",
    "amount": 5
})
blockchain.add_transaction({
    "from": "Charlie",
    "to": "Alice",
    "amount": 3
})

# Mine a new block containing the pending transactions.
blockchain.mine_pending_transactions("miner_address")

# Print the balance of each address.
print(f"Alice's balance: {blockchain.get_balance('Alice')}")
print(f"Bob's balance: {blockchain.get_balance('Bob')}")
print(f"Charlie's balance: {blockchain.get_balance('Charlie')}")

# Add some more transactions to the pending transactions list.
blockchain.add_transaction({
    "from": "Alice",
    "to": "Bob",
    "amount": 1
})
blockchain.add_transaction({
    "from": "Bob",
    "to": "Charlie",
    "amount": 2
})
blockchain.add_transaction({
    "from": "Charlie",
    "to": "Alice",
    "amount": 3
})

# Mine another block containing the new transactions.
blockchain.mine_pending_transactions("miner_address")

# Print the balance of each address again.
print(f"Alice's balance: {blockchain.get_balance('Alice')}")
print(f"Bob's balance: {blockchain.get_balance('Bob')}")
print(f"Charlie's balance: {blockchain.get_balance('Charlie')}")
