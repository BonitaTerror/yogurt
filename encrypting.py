import base64
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend

def prompt_new_password():
    new_password = getpass.getpass('Enter a new password: ')
    password_check = getpass.getpass('Re-enter your password: ')
    if new_password != password_check:
        print('Your passwords need to match')
        return prompt_new_password()
    else:
        return new_password
