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
        if json.loads(headers)!=None:
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
