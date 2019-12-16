import csv
from unit.log import log
from config import csv_path


def opencsvlist():
    data = []
    with open(csv_path) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            data.append(row)
    return data


def opencsvdict():
    log.info('正在读取csv中接口信息')
    '''
    :return:
    eg:
        [{'ID': '1', '项目': '', '模块': '', '用例描述': '', '请求url': 'http://localhost:8282/login/123&123', '请求方式': 'GET',
     '请求数据': '', '预期结果': "{'code': 1}", '返回报文': "{'code': 1}", '测试结果': '成功', '测试人员': ''},
      {'ID': '1', '项目': '', '模块': '', '用例描述': '', '请求url': 'http://localhost:8282/login/123&123', '请求方式': 'GET',
       '请求数据': '', '预期结果': "{'code': 1}", '返回报文': "{'code': 1}", '测试结果': '成功', '测试人员': ''}]
    '''
    data = []
    with open(csv_path) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            data.append(row)
    return data


def writecsv(data):
    log.info('正在将测试结果和返回报文写入csv')
    '''
    eg:
        data = [{'ID': '1', '项目': '', '模块': '', '用例描述': '', '请求url': 'http://localhost:8282/login/123&123', '请求方式': 'GET',
         '请求数据': '', '预期结果': "{'code': 1}", '返回报文': "{'code': 1}", '测试结果': '成功', '测试人员': ''},
        {'ID': '1', '项目': '', '模块': '', '用例描述': '', '请求url': 'http://localhost:8282/login/123&123', '请求方式': 'GET',
         '请求数据': '', '预期结果': "{'code': 1}", '返回报文': "{'code': 1}", '测试结果': '成功', '测试人员': ''}]
    :param data:
    :return:
    '''
    for d in data:
        for k, v in d.items():
            d.update({k: v.replace('"', "'").replace('\n', '\\n')})
    with open(csv_path, 'w') as f:
        headers = ['ID', '项目', '模块', '用例描述', '请求url', '请求方式', '请求头', '请求数据', '预期结果', '返回报文', '测试结果', '测试人员']
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(data)
    return True


if __name__ == '__main__':
    print(os.path.dirname(__file__))
    print(opencsvdict())
