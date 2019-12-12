import requests
from unit.log import log


def req(data):
    log.info('正在请求接口')
    result = []
    for d in data:
        id = d.get('ID')
        url = d.get('请求url')
        method = d.get('请求方式')
        headers = d.get('请求头')
        data = d.get('请求数据')
        if method == 'GET':
            try:
                r = requests.get(url=url, headers=headers)
                result.append({'ID': id, '返回报文': r.text})
            except Exception as e:
                log.warning(e)
                result.append({'ID': id, '返回报文': '请求失败'})
        elif method == 'POST':
            try:
                r = requests.post(url=url, data=data, headers=headers)
                result.append({'ID': id, '返回报文': r.text})
            except Exception as e:
                log.warning(e)
                result.append({'ID': id, '返回报文': '请求失败'})
        else:
            return 'no request type'
    return result
