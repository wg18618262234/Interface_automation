from unit.csvs import opencsv, writecsv
from unit.req import req
from unit.check import check
import logging

logging.info('接口自动化正在启动')
data = opencsv()
result = req(data)
new_data = check(data, result)
writecsv(new_data)
