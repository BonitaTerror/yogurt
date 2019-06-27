import sys
import argparse
import addresses as addr
from yogurt_address_dao import YogurtAddressDao

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
        parser.add_argument('wallet_name')
        args = parser.parse_args(sys.argv[2:])
        address = addr.generate_address()
        address_dao = YogurtAddressDao(args.wallet_name)
        address_dao.save_address(address)


if __name__ == '__main__':
    YogurtParser()
