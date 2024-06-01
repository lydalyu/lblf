from django.shortcuts import render
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login as logIn, logout as logOut
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
from .. import modelForms
from .. import models

@csrf_exempt
@api_view(['POST'])
def login(request):
    if request.method == "POST":
        form = modelForms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data["email"], password=form.cleaned_data["password"])
            if user != None:
                logIn(request, user)
                user_dict = model_to_dict(user)
                return Response({'message': 'ok', 'user' : user_dict})
            else:
                return Response({'message': 'Password and/or Email is not correct '})
    return Response({'message': 'error, you schoul send post request'})

@csrf_exempt
@api_view(['POST'])
def register(request):
    if request.method == "POST":
        form = modelForms.RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] != form.cleaned_data['password_confirm']:
                return Response({'message': 'Password and Password confirmation should be the same'})
            existed_user = models.User.objects.filter(email=form.cleaned_data['email'])
            if existed_user:
                return Response({'message': 'This email is already registed.'})
            try:
                user = models.User.objects.create_user(username=form.cleaned_data['email'],email=form.cleaned_data['email'], password=form.cleaned_data['password'])
                user.save()
            except IntegrityError:
                return Response({'message': 'Registration error'})
            return Response({'message': 'You are successfully registed. Click "Login" to go to the login form.'})
        return Response({'message': 'Form not valid.'})
    return Response({'message': 'Method not allowed.'})

@api_view(['GET'])
def logout(request):
    logOut(request)
    return Response({'message': 'Ok'})