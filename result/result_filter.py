from execution_chain.filter import Filter
from result.handler import result_validator_delegate


class ResultHandlerFilter(Filter):
    """
     将excel中获取的数据用于请求后台，并获取结果
    """

    def do_filter(self, case_holder):
        print("result handler check the result")
        cases = case_holder.get_cases()
        for case in cases:
            through = result_validator_delegate.valid(case.get_check_expression(), case.get_response_holder())
            case.set_through(through)
        print("result handler valid all case")
        self.chain.execute_internal(case_holder)
