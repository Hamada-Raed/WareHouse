from django.urls import path
from . import views
app_name = 'myapp'


urlpatterns = [
    path('', views.index),
    # Add by: Kareem / Render Dashboard Page
    path('Dashboard', views.pageDashboard, name='Dashboard'),
    path('pageLogin', views.pageLogin),  # Page: Login / Kareem
    path('pageRegister', views.pageRegister),  # Page: Login / Kareem
    path('pageDashboard', views.pageDashboard),  # Page: Dashboard / Kareem
    path('pageEnterProducts', views.pageEnterProducts), # Page: Enter Products (Work in Progress) / Kareem
]
