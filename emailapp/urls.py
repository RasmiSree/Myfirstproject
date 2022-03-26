from django.urls import path,include
from emailapp.views import stdform

urlpatterns = [
    path('',stdform,name='stdform')

]