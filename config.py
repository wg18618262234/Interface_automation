import os

csv_path = os.path.dirname(__file__) + '/static/uploads/Interface_automation.csv'
csv_error_path = os.path.dirname(__file__) + '/static/uploads/Interface_automation_error.csv'
csv_success_path = os.path.dirname(__file__) + '/static/uploads/Interface_automation_success.csv'

ding_secret = 'SEC7663fb83e3bbaa067d1b97dee93893d3f3414ff1fb25cb5f5e3012d862bb0e4b'
ding_access_token = '976f344b12655ab5751742a28967f99c1183780eaed3332089c22ae86b7c5959'
ding_url = 'https://oapi.dingtalk.com/robot/send'
