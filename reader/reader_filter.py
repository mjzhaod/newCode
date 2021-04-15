from execution_chain.filter import Filter
import reader.test_case_handler as excel_handler


class ExcelReaderFilter(Filter):
    """
     用于读取excel里的数据，并封装到测试结构文件中
    """

    excel_handler = excel_handler

    def do_filter(self, case_holder):
        print("file reader begin read excel")
        case_definition = case_holder.get_definition()
        cases = excel_handler.handler_excel(case_definition)
        case_holder.set_cases(cases)
        print("file reader read excel complete")
        self.chain.execute_internal(case_holder)


