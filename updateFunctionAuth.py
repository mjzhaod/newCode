import requests
import json
import openpyxl
from request import request
from do_request import do_request,build_url
import data_base

testCase = openpyxl.load_workbook(r"/Users/canyueyinxue/newCode/testcase/功能权限.xlsx")
sheet=testCase.get_sheet_by_name(r"功能权限")
urls=''
headers=''
request_parameter=''

for rownum in range(2,sheet.max_row+1):
    urls=sheet.cell(row=rownum,column=3).value
    headers=sheet.cell(row=rownum,column=4).value
    request_method=sheet.cell(row=rownum,column=5).value
    request_parameter=sheet.cell(row=rownum,column=6).value
    urls=build_url(urls,data_base.token)
    print(urls)
    r=request(urls,request_method,request_parameter,headers=headers)
    response=do_request(r)

    print(headers)
    print(request_parameter)
    print(response.status_code)
    print(response.text)
