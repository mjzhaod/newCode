class ResponseHolder:
    code = None
    response = None
    result = None

    def __init__(self, code, response, result):
        self.code = code
        self.response = response
        self.result = result

    def get_code(self):
        return self.code

    def get_response(self):
        return self.response

    def get_result(self):
        return self.result
