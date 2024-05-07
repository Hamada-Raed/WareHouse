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
    return render(request, 'pageLogin.html') 

#Page: Login Page
def pageLogin(request):
    return render(request, 'pageLogin.html')

#Page: Register page
def pageRegister(request):
    return render(request,'pageRegister.html')

#Page: Dashboard Page
def pageDashboard(request):
    return render(request, 'pageDashboard.html')

#Page: Enter Products Page
def pageEnterProducts(request):
    return render(request, 'pageEnterProducts.html')

