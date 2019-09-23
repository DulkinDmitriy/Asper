class InvalidRequest:
    def __init__(self):
        self.errors = []

    def add_error(self, parameter, message):
        self.errors.append({'parameter': parameter, 'message': message})

    def has_errors(self):
        return len(self.errors) > 0

    def __nonzero__(self):
        return False
    
    __bool__ = __nonzero__

class ValidRequest:
    @classmethod
    def from_dict(self, adict):
        raise NotImplementedError

    def __nonzero__(self):
        return True

    def validate(self):
        raise NotImplementedError

    __bool__ = __nonzero__
