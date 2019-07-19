import os
import time

from django.core.cache import cache
from django.http import JsonResponse

from Swiper.settings import MEDIA_ROOT
from common import errors, cache_keys
from common.utils import is_phone_num
from libs.http import render_json
from user import logics
from user.forms import ProfileForm
from user.models import User


def verify_phone(request):
    """
    # 1、验证手机格式
    # 2、生成验证码
    # 3、保存验证码
    # 4、发送验证码

    :param request:
    :return:
    """
    phone_num = request.POST.get('phone_num')

    if is_phone_num(phone_num):
        # 生成验证码
        # 发送验证码
        if logics.send_verify_code(phone_num):
            return render_json()
        else:
            return render_json(code=errors.SMS_SEND_ERR)
    else:
        return render_json(code=errors.PHONE_NUM_ERR)


def login(request):
    """
    通过验证码登录或注册接口
    如果手机号已存在，则登录，否则，注册

    # 1、检测验证码是否正确
    # 2、注册或登录

    :param request:
    :return:
    """
    phone_num = request.POST.get('phone_num', '')
    code = request.POST.get('code', '')

    phone_num = phone_num.strip()
    code = code.strip()

    cached_code = cache.get(cache_keys.VERIFY_CODE_KEY_PREFIX.format(phone_num))

    if cached_code != code:
        return render_json(code=errors.VERIFY_CODE_ERR)

    # try:
    #     user = User.obejcts.get(phonenum=phone_num)
    # except User.DoesNotExist:
    #     user = User.objects.cereate(phonenum=phone_num)

    # 如果存在 记录，则 get，否则 create
    user, created = User.objects.get_or_create(phonenum=phone_num)

    # 设置登录状态
    request.session['uid'] = user.id

    # token 认证方式
    # 为当前登录用户生成一个 token，并且存储到 缓存中，key为：token:user.id，Value为：token
    # token = user.get_or_create_token()
    # data = {'token': token}
    # return render_json(data=data)

    return render_json(data=user.to_dict())


def get_profile(request):
    user = request.user

    return render_json(data=user.profile.to_dict(exclude=['auto_play']))


def set_profile(request):
    user = request.user

    form = ProfileForm(data=request.POST, instance=user.profile)

    if form.is_valid():
        form.save()
        return render_json()
    else:
        return render_json(data=form.errors)




def upload_head_photo(request):
    print('welcome to you user')

    user = request.user


    print(user)
    #
    # vs = request.POST.get('vs')
    #
    # print(vs)

    head_photo = request.FILES.get('pic')


    print(head_photo)

    file_name = 'avater-{}'.format(int(time.time()))

    file_path = os.path.join(MEDIA_ROOT, file_name)
    print(file_name)

    with open(file_path, 'wb+') as fp:

        for chunk in head_photo.chunks():
            fp.write(chunk)

    return render_json()


def test(request):

    # user = request.user

    # testnum = request.POST.get('num')
    head_photo = request.FILES.get('pic')

    print('head_photo', head_photo)

    file_name = 'avater-{}'.format(int(time.time()))

    file_path = os.path.join(MEDIA_ROOT, file_name)

    print(file_name)

    with open(file_path, 'wb+') as fp:

        for chunk in head_photo.chunks():
            fp.write(chunk)

    return render_json()