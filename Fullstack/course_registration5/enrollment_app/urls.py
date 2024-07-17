from django.urls import path
from .views import *

urlpatterns = [
    path('enrollment', homefun, name='homefunvar'),
    path('registration/', formfun, name='formfunvar'),
]

