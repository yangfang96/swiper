from django.shortcuts import render

from libs.http import render_json
from social.logics import *

def recommend(request):

    user = request.user

    rec_users = logics.recommend_users(user)

    users = [u.to_dict() for u in rec_users]

    return render_json(data=users)



def like(request):
    # 登录的一种判断方式
    user = request.user
    sid = request.POST.get('sid')

    if sid is None:
        return render_json(code=errors.SID_ERR)

    sid = int(sid)

    matched = logics.like_someone(user.id, sid)

    return render_json(data={'matched': matched})


def dislike(request):
    return None


def superlike(request):
    return None


def rewind(request):
    return None


def liked_me(request):
    return None