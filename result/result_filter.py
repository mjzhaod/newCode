from execution_chain.filter import Filter


class ResultHandlerFilter(Filter):
    """
     将excel中获取的数据用于请求后台，并获取结果
    """

    request_handler = None

    def do_filter(self, case_holder):
        print("result handler check the result")
        self.chain.execute(case_holder)
