"""Pyplan Engine URL Configuration
"""
from django.urls import path

from pyplan_engine.application import views

urlpatterns = [
    path('test', views.test),
    path('status', views.getStatus),
    path('checkRead', views.checkRead),
    path('checkWrite', views.checkWrite),
    path('healthcheck', views.healthCheck),
    path('cmdtest', views.cmdtest),
]
