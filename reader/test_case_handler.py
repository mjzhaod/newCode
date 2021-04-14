import reader.excel.reader as excel_reader
from case.case import Case
from reader.excel.reader import ResultSet
from case.test_case_definition import TestCaseDefinition
from reader.excel.reader import QueryInfoHolder
from reader.excel.reader import FileReaderInfoHolder


def handler_excel(case_definition: TestCaseDefinition):
    properties = case_definition.get_properties()
    path = case_definition.get_path()
    ensure_valid_file_path(path)
    query_info = build_query_info(properties)
    return excel_reader.read(FileReaderInfoHolder(query_info, path, None, result_handler))


def result_handler(result_set: ResultSet) -> Case:
    """
        将读取的excel值封装到用例中
      :param result_set:
      :return:
      """
    return Case(result_set.get_by_name("id"), result_set.get_by_name("description"), result_set.get_by_name("headers"),
                result_set.get_by_name("method"), result_set.get_by_name("url"),
                result_set.get_by_name("check_expression"), result_set.get_by_name("params"))


def build_query_info(properties):
    query_info = []
    for prop in properties:
        index = prop.get_index()
        if index is None:
            raise Exception("excel 列号不合法")
        query_info.append(QueryInfoHolder(index, prop.get_name()))
    return query_info


def ensure_valid_file_path(path: str):
    if path is None or path == "":
        raise Exception("excel 文件不合法")
    if not path.endswith('xlsx'):
        raise Exception("不支持excel格式，当前只支持xls")


