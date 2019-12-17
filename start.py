from unit.csvs import open_csv_dict, write_csv, write_csv_success, write_csv_error
from unit.req import req
from unit.check import check
from unit.log import log


def start(headers):
    log.info('接口自动化正在启动')
    data = open_csv_dict()
    result = req(data, headers)
    new_data = check(data, result)
    write_csv(new_data)
    write_csv_success()
    write_csv_error()
