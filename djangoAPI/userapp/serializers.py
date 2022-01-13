from functools import partial
from rest_framework import serializers
from userapp.models import Users

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('id','first_name','last_name','company_name','city','state','zip','email','web','age')
