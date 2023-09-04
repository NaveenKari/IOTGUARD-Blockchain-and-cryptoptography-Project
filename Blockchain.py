
import datetime
import hashlib
import uuid
import json
from flask import Flask, jsonify

import requests
import atexit




class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0',data='ee')
    def id():
        return str(uuid.uuid4())   
    def create_block(self, proof, previous_hash,data):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'data':data}
        self.chain.append(block)
        with open('blockchain_data.json', 'w') as f:
            json.dump(self.chain, f)
        
        return block
    def print_previous_block(self):
        return self.chain[-1]
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:5] == '00000':
                check_proof = True
            else:
                new_proof += 1
 
        return new_proof
    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
 
    def chain_valid(self, chain):
        if not chain:
            raise False

        previous_block = chain[0]
        block_index = 1
 
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
 
            previous_proof = previous_block['proof']
            proof = block['proof']

            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
 
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1
 
        return True
blockchain = Blockchain()
@atexit.register
def save_blockchain_data():
    with open('blockchain_data.json', 'w') as f:
        json.dump(blockchain.chain, f)

def Mine():
    # Replace the URL with the address of your Flask app
    url = 'http://127.0.0.1:5000/mine_block'

    # Send a GET request to mine a block
    response = requests.get(url)

    # Print the response from the server
    print(response.json())


app = Flask(__name__)



@app.route('/mine_block', methods=['GET'])
def mine_block():
    previous_block = blockchain.print_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    data=Blockchain.id()
    block = blockchain.create_block(proof, previous_hash,data)
    response = {'message': 'A block is MINED',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'data':block['data']}
               
    return jsonify(response), 200
@app.route('/get_chain', methods=['GET'])
def display_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200
@app.route('/valid', methods=['GET'])
def valid():
    valid = blockchain.chain_valid(blockchain.chain)
 
    if valid:
        response = {'message': 'The Blockchain is valid.'}
    else:
        response = {'message': 'The Blockchain is not valid.'}
    return jsonify(response), 200

app.run(host='127.0.0.1', port=5000)


