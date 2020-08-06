from passlib.hash import pbkdf2_sha256


class YogurtBtcAddress():

    def __init__(self, address, password=None):
        self.password = pbkdf2_sha256.hash(password) if password else None
        self.address = address

    def verify_password(self, password):
        return pbkdf2_sha256.verify(password, self.password)
