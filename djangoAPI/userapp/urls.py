from django.urls import re_path
from userapp import views

urlpatterns=[
    re_path(r'^user$',views.userlistApi),
    re_path(r'^user/([0-9]+)',views.userApi),
]