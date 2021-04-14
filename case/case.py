class Case:
    id = None
    description = None
    headers = None
    method = None
    url = None
    check_expression = None
    params = None
    response_holder = None
    through = None

    def __init__(self, id, description, headers, method, url, check_expression, params):
        self.id = id
        self.description = description
        self.headers = headers
        self.method = method
        self.url = url
        self.check_expression = check_expression
        self.params = params

    def get_id(self):
        return self.id

    def get_description(self):
        return self.description

    def get_headers(self):
        return self.headers

    def get_method(self):
        return self.method

    def get_url(self):
        return self.url

    def get_check_expression(self):
        return self.check_expression

    def set_response_holder(self, response_holder):
        self.response_holder = response_holder

    def get_response_holder(self):
        return self.response_holder

    def get_through(self):
        return self.through

    def set_through(self, through):
        self.through = through
