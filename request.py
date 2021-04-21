class Request():
    url = None
    method = None
    param = None
    body = None
    headers = None
    cookies = None
    expectResult = None


    def __init__(self,url,method,body,expectResult,param=None,headers=None,cookies=None):
        self.url=url
        self.method = method
        self.param = param
        self.body = body
        self.expectResult=expectResult
        self.headers = headers
        self.cookies = cookies

    def __init__(self):
       pass
