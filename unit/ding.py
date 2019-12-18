import time
import hmac
import hashlib
import base64
from urllib.parse import quote_plus
import json
import requests
from config import ding_secret, ding_access_token, ding_url


def get_sign():
    timestamp = round(time.time() * 1000)
    secret = ding_secret
    secret_enc = bytes(secret, encoding='utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = bytes(string_to_sign, encoding='utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = quote_plus(base64.b64encode(hmac_code))
    return {'timestamp': timestamp, 'sign': sign}


def send_message(message, **kwargs):
    timestamp = kwargs.get('timestamp')
    sign = kwargs.get('sign')
    url = '{}?access_token={}&timestamp={}&sign={}'.format(ding_url, ding_access_token, timestamp, sign)
    data = json.dumps(
        {
            "msgtype": "markdown",
            "markdown": {
                "title": "测试报告",
                "text": message,
            },
            "at": {
                "atMobiles": [
                ],
                "isAtAll": True
            }
        }
    )
    headers = {'Content-Type': 'application/json'}
    r = requests.post(url=url, data=data, headers=headers)
    raw = r.text
    return raw
