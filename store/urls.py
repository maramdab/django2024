from django.urls import path,include
from .views import *

urlpatterns = [
    path('',products,name='products'),
    path('home/',home,name='home')
]