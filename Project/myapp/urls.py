from django.urls import path     
from . import views
app_name = 'myapp'


urlpatterns = [
    path('', views.index),
    path('pageLogin', views.pageLogin), # Page: Login / Kareem
    path('pageRegister', views.pageRegister), # Page: Login / Kareem
    path('pageDashboard', views.pageDashboard), # Page: Dashboard / Kareem
    path('pageEnterProducts', views.pageEnterProducts) # Page: Enter Products / Kareem
]