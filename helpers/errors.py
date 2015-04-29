class ApiError(Exception):
    def __init__(self, msg, code=1):
        Exception.__init__(self)
        self.msg = msg
        self.code = code
