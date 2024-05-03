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

