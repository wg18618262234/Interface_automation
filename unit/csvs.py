import csv
from unit.log import log
from config import csv_path, csv_error_path, csv_success_path


def open_csv_list():
    data = []
    with open(csv_path) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            data.append(row)
    return data


def open_csv_dict():
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


def open_success_csv_dict():
    data = []
    with open(csv_success_path) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            data.append(row)
    return data


def open_success_csv_list():
    data = []
    with open(csv_success_path) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            data.append(row)
    return data


def open_error_csv_dict():
    data = []
    with open(csv_error_path) as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            data.append(row)
    return data


def open_error_csv_list():
    data = []
    with open(csv_error_path) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            data.append(row)
    return data


def write_csv(data):
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


def write_csv_error():
    data_error = []
    data = open_csv_dict()
    for d in data:
        if d.get('测试结果') == '失败':
            data_error.append(d)
    with open(csv_error_path, 'w') as f:
        headers = ['ID', '项目', '模块', '用例描述', '请求url', '请求方式', '请求头', '请求数据', '预期结果', '返回报文', '测试结果', '测试人员']
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(data_error)
    return True


def write_csv_success():
    data_success = []
    data = open_csv_dict()
    for d in data:
        if d.get('测试结果') == '成功':
            data_success.append(d)
    with open(csv_success_path, 'w') as f:
        headers = ['ID', '项目', '模块', '用例描述', '请求url', '请求方式', '请求头', '请求数据', '预期结果', '返回报文', '测试结果', '测试人员']
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(data_success)
    return True


def get_count():
    count = {
        'success_count': 0,
        'error_count': 0
    }
    sc = 0
    ec = 0
    s_c = open_success_csv_list()
    for s in s_c:
        sc += 1
    e_c = open_error_csv_list()
    for e in e_c:
        ec += 1
    sc = sc - 1
    ec = ec - 1
    count.update({'success_count': sc, 'error_count': ec})
    return count

