import requests
from django.conf import settings

from common import config


def send_verify_code(phone, code):
    print('send verify code:', phone, code)
    if settings.DEBUG:
        print('send verify code:', phone, code)
        return True

    params = config.YZX_SMS_PARAMS.copy()

    params['mobile'] = phone
    params['param'] = code

    resp = requests.post(config.YZX_SMS_URL, json=params)

    if resp.status_code == 200:
        ret = resp.json()
        print(ret)
        if ret.get('code') == '103126':
            return True

    return False
