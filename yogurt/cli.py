import sys
import pickle
import argparse
from .crypto import AESCipher
from .addresses import YogurtBtcAddress, generate_address


class YogurtParser():

    def __init__(self):
        parser = argparse.ArgumentParser(
                        description='Yogurt CLI Bitcoin Wallet',
                        usage='yogurt <command> [<args>]')
        parser.add_argument('command', help='Subcommand to run')

        args = parser.parse_args(sys.argv[1:2])
        if not hasattr(self, args.command):
            print('Unrecognized command')
            parser.print_help()
            exit(1)

        getattr(self, args.command)()

    def create(self):
        parser = argparse.ArgumentParser(
                        description='Create a new Yogurt Wallet')
        parser.add_argument('wallet_path')
        parser.add_argument('-e', action='store_true')  # option for encrypting
        args = parser.parse_args(sys.argv[2:])

        address = generate_address()

        if args.e:
            password = AESCipher.prompt_new_password()
            cipher = AESCipher(password)

            ygrt_addr = YogurtBtcAddress(address, password)

            pkl = pickle.dumps(ygrt_addr.address)
            encrypted_pkl = cipher.encrypt(pkl)

            with open(args.wallet_path, 'wb') as f:
                pickle.dump(encrypted_pkl, f)
        
        else:
            ygrt_addr = YogurtBtcAddress(address)
            with open(args.wallet_path, 'wb') as f:
                pickle.dump(ygrt_addr.address, f)



if __name__ == '__main__':
    YogurtParser()
