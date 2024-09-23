
from django.contrib import admin
from django.urls import path
from myproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jobfeedpage/', jobfeedpage,name='jobfeedpage'),
    path('', loginPage,name='loginPage'),
    path('register/', register,name='register'),
    path('logoutPage/', logoutPage,name='logoutPage'),
    path('base/', base,name='base'),
]
