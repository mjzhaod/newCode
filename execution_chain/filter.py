class Filter:

    chain = None

    def __init__(self):
        pass

    def do_filter(self, case_holder):
        raise Exception("不合法Filter")

    def set_chain(self, chain = None):
        self.chain = chain
