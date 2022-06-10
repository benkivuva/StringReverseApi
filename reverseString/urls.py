from rest_framework.routers import DefaultRouter
from django.urls import path
from .apiviews import *


urlpatterns = [
    path('', ReversedStringsView.as_view(), name='createaphrase'),

]