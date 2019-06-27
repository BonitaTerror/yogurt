import pybtc

def generate_address():
    priv = pybtc.create_private_key()
    address = pybtc.Address(priv)
    return address

def address_from_private_key(priv):
    return pybtc.Address(priv)
