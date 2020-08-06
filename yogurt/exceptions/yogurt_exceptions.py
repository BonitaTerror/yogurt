class YogurtException(Exception):
    pass


class YogurtWrongPasswordException(YogurtException):

    def __init__(self):
        self.data = 'Incorrect password for yogurt address'
