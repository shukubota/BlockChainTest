import hashlib
import json
from time import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # create block  add chain
        pass

    def new_transaction(self, sender, recipient, amount):
        # add new transaction
        self.current_trancsactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        #hashed a block
        pass

    @property
    def last_block(self):
        # return the last block in the chain
        pass
