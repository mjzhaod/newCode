from execution_chain.execution_chain import TestExecutionChain
from reader.reader_filter import ExcelReaderFilter
from request.request_filter import RequestFilter
from result.result_filter import ResultHandlerFilter
from case.test_case_definition import TestCaseDefinition
from case.property_definition import Property


class ExecutionChainFactory:

    @staticmethod
    def instance():
        # 定义执行链对象
        filters = [ExcelReaderFilter, RequestFilter, ResultHandlerFilter]
        execution_chain = TestExecutionChain(filters)
        # 添加filter
        return execution_chain


def startup():
    execution_chain = ExecutionChainFactory.instance()
    case_definition = TestCaseDefinition("/Users/hong/Downloads/功能权限.xlsx",
                                         [Property("id", 0), Property("description", 1), Property("url", 2),
                                          Property("headers", 3), Property("method", 4), Property("params", 5),
                                          Property("check_expression", 6)])
    execution_chain.execute(case_definition)


startup()


