import re
import random


PHONE_PATTERN = re.compile(r'^1[3-9]\d{9}$')


def is_phone_num(phone_num):
    """
    验证手机号码格式
    :param phone_num:
    :return:
    """

    return True if PHONE_PATTERN.match(str(phone_num).strip()) else False


def gen_random_code(length=4):

    if not isinstance(length, int):
        length = 1

    if length <= 0:
        length = 1

    code = random.randrange(10**(length-1),10**length)

    return str(code)



if __name__ == '__main__':


    # res = is_phone_num('14554885655')

    code = gen_random_code(length=4)
    print(code)

    # print(res)
