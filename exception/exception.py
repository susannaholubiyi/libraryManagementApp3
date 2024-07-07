class BookNotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super.__init__(self.message)


class UserNotFoundException(Exception):
    def __init__(self, message):
        self.message = message
        super.__init__(self.message)


class LoginFailedException(Exception):
    def __init__(self, message):
        self.message = message
        super.__init__(self.message)