import os
# import pybtc
import pickle
from yogurt_exceptions import YogurtWrongPasswordException


class YogurtAddressDao():

    def __init__(self, wallet_path):
        self.path = os.path.abspath(wallet_path)

    def save_address(self, address):
        with open(self.path, 'wb') as file:
            pickle.dump(address, file)

    def load_address(self):
        with open(self.path, 'rb') as file:
            address = pickle.load(file)
            return address

    def save_address_encrypted(self, yogurt_address, cipher):
        serialized_address = pickle.dumps(yogurt_address.address)

        encrypted_address = cipher.encrypt(serialized_address)
        yogurt_address.address = encrypted_address

        with open(self.path, 'wb') as file:
            pickle.dump(yogurt_address, file)

    def load_address_encrypted(self, password, cipher):
        with open(self.path, 'rb') as file:
            yogurt_address = pickle.load(file)

        if yogurt_address.verify_password(password):
            serialized_address = cipher.decrypt(yogurt_address.address)
            address = pickle.loads(serialized_address)
            yogurt_address.address = address
            return yogurt_address
        else:
            raise YogurtWrongPasswordException()
