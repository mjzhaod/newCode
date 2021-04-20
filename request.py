class Request():

    def __init__(self,url,method,body,param=None,headers=None,cookies=None):
        self.url=url
        self.method = method
        self.param = param
        self.body = body
        self.headers = headers
        self.cookies = cookies

    def __init__(self):
       pass
