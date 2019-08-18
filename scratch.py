import hashlib
import json
from time import time
from uuid import uuid4

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Creates a new Block and adds it to the chain
        pass

    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        pass

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass

#block specifics
    block = {
        'index' :
        'timestamp' :
        'transactions' : [
        {
            'sender' :
            'recipient' :
            'amount' :
        }
    ]
        'proof' :
        'previous_hash' :
    }

# code for new transaction

class Blockchain(object):

    def new_transaction(self, sender, recipient, amount):
        """
        #Creates a new transationc to go into the next mined Block

        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender' : sender,
            'recipient' : recipient,
            'amount' : amount,
        })

        return self.last_block[ 'index' ] + 1

        @property
        def last_block(self):
            return self.chain[-1]


# Instantiate our Node
    app = Flask(__name__)

# Generate a globally unique address for this node
    node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
    blockshain = Blockchain()

@app.route('/mine', methods=['GET'])
    def mine(self):
        return "We'll mine a new Block"

@app.route('/transactions/new', methods=['POST'])
def new_transactions():
    return "We'll add a new transaction"

@app.route('/chain', methods=['GET'])
def full_chain()""
         response = {
             'chain' : blockchain.chain,
             'length' : len(blockchain.chain),
         }
         return jsonify(response), 200

if __name__ == '__main__' :
    app.run(host='0.0.0.0.' , port=5000)
