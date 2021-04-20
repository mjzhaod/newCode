import requests
import json
import openpyxl
from request import Request
from do_request import do_request,build_url
import data_base


def generate_result(row_num, columns):
    re = Request()
    for column in columns:
        value = sheet.cell(row_num, column["index"]).value
        setattr(re, column["name"], value)
    return re


workbook = openpyxl.load_workbook(r"/Users/hong/Downloads/功能权限.xlsx")
sheet=workbook.get_sheet_by_name(r"功能权限")
urls=''
headers=''
request_parameter=''

for rownum in range(2,sheet.max_row+1):
    # 定义excel里的一列 对应request对象里的字段 name表示request里的属性名， index表示excel的列号
    request = generate_result(rownum, [{"name": "url", "index": 3}, {"name": "headers", "index": 4},
                                         {"name": "method", "index": 5},
                                         {"name": "body", "index": 6}])
    urls = build_url(request, data_base.token)
    print(urls)
    response=do_request(request)

    print(headers)
    print(request_parameter)
    print(response.status_code)
    print(response.text)


