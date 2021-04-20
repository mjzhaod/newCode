import requests
import json
import request

def do_request(request):
    url=request.url
    method=request.method
    param=request.param
    body=request.body
    headers=request.headers
    cookies=request.cookies


    if method== 'get':
        response=request.get(url)
    if method== 'post':
        if json.loads(headers) is not None:
            response=requests.post(url=url,headers=json.loads(headers),data=json.dumps(json.loads(body)))
        else:
            response=requests.post(url=url,data=json.dumps(json.loads(body)))
    return response


def build_url(request,url_param):
    url = request.url
    if url.find('?') == -1:
        url=url+'?authoToken='+url_param
    else:
        url=url+'&authoToken='+url_param
    request.url = url


def check(request):
    result=do_request(request)
    if result.response_status==200:
        return result.text
    elif (result.status_code == 401):
        raise Exception("用户没有登陆")
    else:
        raise Exception("服务器错误" + str(result.status_code))


