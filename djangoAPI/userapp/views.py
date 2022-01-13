from functools import partial
from tkinter.messagebox import NO
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.paginator import Paginator,EmptyPage

from userapp.models import Users
from userapp.serializers import UsersSerializer
from django.db.models import Q

# Create your views here.
@csrf_exempt
def userApi(request,id=0):
    if request.method == 'GET':
        users = Users.objects.get(id=id)
        users_serializer = UsersSerializer(users)
        return JsonResponse(users_serializer.data,safe=False)
    elif request.method == 'PUT':
        users_data = JSONParser().parse(request)
        users = Users.objects.get(id=id)
        users_serializer=UsersSerializer(users,data=users_data,partial=True)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse("Userdata Updated Successfully",safe=False)
        return JsonResponse("Failed to Update")
    elif request.method == 'DELETE':
        users = Users.objects.get(id=id)
        users.delete() 
        return JsonResponse("User Deleted Successfully",safe=False)
@csrf_exempt
def userlistApi(request):
    if request.method == 'GET':
        users = Users.objects.all()
        namekey = request.GET.get('name',None)
        sortkey = request.GET.get('sort',None)
        limitkey = int(request.GET.get('limit',5))
        pagekey = int(request.GET.get('page',1))

        if sortkey is not None:
            users=users.order_by(sortkey)
        if namekey is not None:
            users = users.filter(Q(first_name__icontains = namekey) | Q(last_name__icontains = namekey))
        if pagekey is not None:
            users= Paginator(users,5)
            try:
              page = users.page(pagekey)
            except EmptyPage:
                page=users.page(1)
            users= page
        if limitkey is not None:
            users = users[:limitkey]
        users_serializer = UsersSerializer(users,many=True)
        return JsonResponse(users_serializer.data,safe=False)
    elif request.method == 'POST':
        users_data = JSONParser().parse(request)
        users_serializer = UsersSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse({"status":200,"msg":"User Added succesfully"},safe=False)
        return JsonResponse("Failed to add user")
