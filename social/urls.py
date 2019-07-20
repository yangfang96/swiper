from django.urls import path
from social import apis


urlpatterns =[
    path('test', apis.test),
]