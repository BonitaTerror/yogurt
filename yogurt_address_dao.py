import os
import pybtc
import pickle

class YogurtAddressDao():

    def __init__(self, wallet_path):
        self.path = os.path.abspath(wallet_path)

    def save_address(self, address):
        with open(self.path, 'wb') as file:
            pickle.dump(address, file)

    def load_address(self):
        with open(self.path, 'r') as file:
            address = pickle.load(file)
            return address
