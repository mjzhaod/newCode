from execution_chain.filter import Filter


class RequestFilter(Filter):
    """
     将excel中获取的数据用于请求后台，并获取结果
    """

    request_handler = None

    def do_filter(self, case_holder):
        print("request invoke the request")
        # cases 是一个数组 ，里面是一个case case的属性有
        #     id = None
        #     description = None
        #     headers = None
        #     method = None
        #     url = None
        #     check_expression = None
        #     params = None
        #     result = None


        cases = case_holder.get_cases()
        for case in cases:
            id = case.id
            pass
        # 发送请求，并获取response的数据，涉及到数据可能有 http code以及返回值
        self.chain.execute(case_holder)
