import requests
from case.response_holder import ResponseHolder
import json

methods = ["POST", "GET", "DELETE", "PUT"]


def handler(case_holder):
    cases = case_holder.get_cases()
    for case in cases:
        response = do_request(case)
        handler_result(response, case)


def do_request(case):
    ensure_valid_case(case)
    method = case.get_method().upper()
    url = build_url(case)
    headers = build_header(case)
    body = build_body(case.get_body())
    response = requests.request(method, url, headers=headers, data=body)
    return response


def ensure_valid_case(case):
    ensure_method(case.get_method())
    ensure_valid_url(case.get_url())


def ensure_method(method: str):
    if method.upper() not in methods:
        raise Exception("不合法请求类型")


def ensure_valid_url(url: str):
    if url is None or url == "":
        raise Exception("url 不能为空")


def build_url(case):
    params = case.get_params()
    url = case.get_url()
    self_url_param = ""
    if params is not None:
        params = json.loads(params)
        for key in params:
            self_url_param += key + "=" + params[key]
    if self_url_param != "":
        if "?" in url:
            url += "&" + self_url_param
        else:
            url += "?" + self_url_param
    if not (url.startswith("http") or url.startswith("https")):
        url = "http://" + url
    return url


def build_header(case):
    headers = case.get_headers()
    # 如果header为空且body不为空， 使用默认。header
    if case.get_body() is not None:
        if headers is None:
            headers = {}
        else:
            headers = json.loads(headers)
        headers["Content-Type"] = "application/json;charset=UTF-8"
    return headers


def handler_result(response, case):
    response_holder = ResponseHolder(response.status_code, response, response.text)
    case.set_response_holder(response_holder)


def build_body(body):
    if body is not None:
        return json.loads(body)
    return None
