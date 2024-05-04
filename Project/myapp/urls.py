from django.urls import path     
from . import views
app_name = 'myapp'


urlpatterns = [
    path('', views.index),
    path('creatAccountpage', views.createAccountpage),
    path('CreateAccountProcess', views.CreateAccountProcess , name='CreateAccountProcess'),
]