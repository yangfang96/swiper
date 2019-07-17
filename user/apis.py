from django.http import JsonResponse

from common.utils import is_phone_num ,gen_random_code
from common import errors
from libs.http import render_json
from user import logics


def verify_phone(request):
    phone_num = request.POST.get('phone_num')


    if is_phone_num(phone_num):

        if logics.send_verify_code(phone_num):

            return render_json()
        else:
            return render_json(code=errors.SMS_SEND_ERR)

    else:
        return render_json(code=errors.PHONE_NUM_ERR)
