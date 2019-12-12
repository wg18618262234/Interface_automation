from unit.csvs import opencsvdict, writecsv
from unit.req import req
from unit.check import check
from unit.log import log


def start():
    log.info('接口自动化正在启动')
    data = opencsvdict()
    result = req(data)
    new_data = check(data, result)
    writecsv(new_data)

start()