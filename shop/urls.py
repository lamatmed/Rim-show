from django.urls import path
from shop.views import *

urlpatterns = [
    path('', index, name='home'),
    
    path('<int:myid>', detail, name='detail'),
    
]