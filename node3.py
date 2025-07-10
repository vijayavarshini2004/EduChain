from flask import Flask, jsonify, request, render_template, redirect
from uuid import uuid4
from blockchain import Blockchain

app = Flask(__name__)
node_id = str(uuid4()).replace('-', '')
blockchain = Blockchain()


@app.route('/')
def index():
    return render_template('index.html', chain=blockchain.chain, nodes=blockchain.nodes)


@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    student = request.form['student']
    degree = request.form['degree']
    institution = request.form['institution']
    blockchain.add_transaction(student, degree, institution)
    return redirect('/')

@app.route('/mine_block', methods=['GET'])
def mine_block():
    prev = blockchain.last_block['proof']
    proof = blockchain.proof_of_work(prev)
    prev_hash = blockchain.hash(blockchain.last_block)
    blockchain.add_transaction(student='System', degree='Block Mined', institution=node_id)
    blockchain.create_block(proof, prev_hash)
    return redirect('/')

@app.route('/get_chain', methods=['GET'])
def get_chain():
    return jsonify(chain=blockchain.chain, length=len(blockchain.chain)), 200

@app.route('/register_node', methods=['POST'])
def register_node():
    url = request.form['node_url']
    blockchain.register_node(url)
    return redirect('/')

@app.route('/sync_chain', methods=['GET'])
def sync_chain():
    blockchain.replace_chain()
    return redirect('/')


if __name__ == '__main__':
    app.run(port=5003)
