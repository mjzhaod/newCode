from execution_chain.filter import Filter
from case.case_info_holder import CaseInfoHolder


class TestExecutionChain:
    filters = None
    index = -1

    def __init__(self, filters):
        self.filters = filters

    def execute_internal(self, case_holder):
        """
        依次获取每个filter，并使用filter进行处理
        :return:
        """
        filter = self.obtain_filter()
        if filter is None:
            return
        # 使用self作为传递参数时，莫名会导致miss parameter 错误，这里直接根据类型传入两个参数
        filter.set_chain(self)
        return filter.do_filter(case_holder)

    def execute(self, case_definition):
        case_holder = CaseInfoHolder(case_definition)
        return self.execute_internal(case_holder)

    def obtain_filter(self) -> Filter:
        """
        获取下一个filter
        :return:
        """

        self.index += 1
        if self.index >= len(self.filters):
            return
        return self.filters[self.index]

