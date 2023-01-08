import hashlib
import time
import urllib.request
import json


class Block:
    def __init__(self, transactions, previous_hash):
        self.timestamp = time.time()
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"{self.previous_hash}{self.timestamp}{self.transactions}{self.nonce}".encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()

    def mine_block(self, difficulty):
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calc_hash()

        print(f"Block mined: {self.hash}")


class Blockchain:
    def __init__(self, node_id):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 4
        self.pending_transactions = []
        self.mining_reward = 100
        self.node_id = node_id

    def create_genesis_block(self):
        return Block([], "0")

    def get_latest_block(self):
        return self.chain[-1]

    def mine_pending_transactions(self, mining_reward_address):
        block = Block(self.pending_transactions, self.get_latest_block().hash)
        block.mine_block(self.difficulty)
        print(f"Block successfully mined!")
        self.chain.append(block)
        self.pending_transactions = [{
            "from": "mining_reward",
            "to": mining_reward_address,
            "amount": self.mining_reward
        }]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)

    def get_balance(self, address):
        balance = 0
        for block in self.chain:
            for trans in block.transactions:
                if trans['from'] == address:
                    balance -= trans['amount']
                if trans['to'] == address:
                    balance += trans['amount']
        return balance
