from django.urls import path

from user import apis

urlpatterns = [
    path('verify-phone', apis.verify_phone),
    path('login', apis.login),
    path('get-profile', apis.get_profile),
    path('set-profile', apis.set_profile),
<<<<<<< HEAD
    path('upload-avatar', apis.upload_avatar),
]
=======
    path('upload', apis.upload_head_photo),
    path('test', apis.test),

]
>>>>>>> develop
