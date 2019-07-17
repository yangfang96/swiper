from django.core.cache import cache
from django.http import JsonResponse

from common.utils import is_phone_num ,gen_random_code
from common import errors, cache_keys
from libs.http import render_json
from user import logics
from user.models import User


def verify_phone(request):
    phone_num = request.POST.get('phone_num')


    if is_phone_num(phone_num):

        if logics.send_verify_code(phone_num):

            return render_json()
        else:
            return render_json(code=errors.SMS_SEND_ERR)

    else:
        return render_json(code=errors.PHONE_NUM_ERR)



def login(request):

    phone_num = request.POST.get('phone_num', '')
    code = request.POST.get('code', '')

    phone_num = phone_num.strip()
    code = code.strip()

    cached_code = cache.get(cache_keys.VERIFY_CODE_KEY_PREFIX.format(phone_num))

    if cached_code != code:
        return render_json(code=errors.VERIFY_CODE_ERR)


    user, created = User.objects.get_or_create(phonenum=phone_num)

    request.session['uid'] = user.id


    return render_json(data=user)
