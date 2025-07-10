import hashlib
import json
from time import time
from uuid import uuid4
from urllib.parse import urlparse
import requests


class Blockchain:
    def __init__(self):
        self.chain = []
        self.transactions = []
        self.nodes = set()
        self.create_block(proof=1, previous_hash='0')

    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.transactions,
            'proof': proof,
            'previous_hash': previous_hash
        }
        self.transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, student, degree, institution):
        self.transactions.append({
            'student': student,
            'degree': degree,
            'institution': institution
        })
        return self.last_block['index'] + 1

    def proof_of_work(self, prev_proof):
        new_proof = 1
        while True:
            hash_val = hashlib.sha256(str(new_proof**2 - prev_proof**2).encode()).hexdigest()
            if hash_val[:4] == '0000':
                return new_proof
            new_proof += 1

    def hash(self, block):
        encoded = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded).hexdigest()

    def is_chain_valid(self, chain):
        prev_block = chain[0]
        for i in range(1, len(chain)):
            block = chain[i]
            if block['previous_hash'] != self.hash(prev_block):
                return False
            if not self.hash_proof_valid(prev_block['proof'], block['proof']):
                return False
            prev_block = block
        return True

    def hash_proof_valid(self, prev, curr):
        hash_val = hashlib.sha256(str(curr**2 - prev**2).encode()).hexdigest()
        return hash_val[:4] == '0000'

    def replace_chain(self):
        longest = self.chain
        for node in self.nodes:
            try:
                response = requests.get(f'http://{node}/get_chain')
                if response.status_code == 200:
                    length = response.json()['length']
                    chain = response.json()['chain']
                    if length > len(longest) and self.is_chain_valid(chain):
                        longest = chain
            except:
                continue
        self.chain = longest
        return True

    @property
    def last_block(self):
        return self.chain[-1]
