class Case:
    id = None
    description = None
    headers = None
    method = None
    url = None
    check_expression = None
    params = None

    def __init__(self, id, description, headers, method, url, check_expression, params):
        self.id = id
        self.description = description
        self.headers = headers
        self.method = method
        self.url = url
        self.check_expression = check_expression
        self.params = params
