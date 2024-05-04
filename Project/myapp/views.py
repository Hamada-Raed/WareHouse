from django.shortcuts import render, redirect
from django.shortcuts import reverse
from .models import *
from .models import Prodcut
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta
from django.views.decorators.csrf import csrf_exempt
import json 


def index(request):
    return render(request, 'index.html') 

#Page: Login Page
def createAccountpage(request):
    return render(request,'pages-register_2.html')

#Process: Create New Account
def CreateAccountProcess(request):
    test = request.POST
    print("This is the test part you Should Read!")
    print(test)
    return render(request, 'pages-register_2.html')
