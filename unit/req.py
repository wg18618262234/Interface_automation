import requests
import logging


def req(data):
    logging.info('正在请求接口')
    result = []
    for d in data:
        id = d.get('ID')
        url = d.get('请求url')
        method = d.get('请求方式')
        headers = d.get('请求头')
        data = d.get('请求数据')
        if method == 'GET':
            r = requests.get(url=url, headers=headers)
            result.append({'ID': id, '返回报文': r.text})
        elif method == 'POST':
            r = requests.post(url=url, data=data, headers=headers)
            result.append({'ID': id, '返回报文': r.text})
        else:
            return 'no request type'
    return result
