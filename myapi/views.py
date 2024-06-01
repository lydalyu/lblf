from django.shortcuts import render
from django.http import HttpResponse
from django.db import IntegrityError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login as logIn, logout as logOut
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from . import modelForms
from . import models

def index(request):
    return render('myapp/index.html')

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})
