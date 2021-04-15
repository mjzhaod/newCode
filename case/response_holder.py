class ResponseHolder:
    code = None
    response = None
    result = None

    def __init__(self, code, response, result):
        self.code = code
        self.response = response
        self.result = result
