from django.urls import path     
from . import views
app_name = 'myapp'


urlpatterns = [
    path('', views.index),
    path('Dashboard', views.Dashboard , name='Dashboard'), # Add by: Kareem / Render Dashboard Page
]