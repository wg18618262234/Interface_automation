import logging


def check(data, result):
    logging.info('正在校验接口正确性')
    for d in data:
        for r in result:
            if r.get('ID') == d.get('ID'):
                d['返回报文'] = r.get('返回报文')
                d['预期结果'] = d.get('预期结果').replace("'", '"')
                if d.get('预期结果').strip('{}').replace(' ', '') in r.get('返回报文').replace(' ', ''):
                    d['测试结果'] = '成功'
                else:
                    d['测试结果'] = '失败'
    return data
