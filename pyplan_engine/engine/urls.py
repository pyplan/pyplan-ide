"""Pyplan Engine URL Configuration
"""
from django.urls import path

from pyplan_engine.engine import views

urlpatterns = [
    path('create', views.createEngine),
    path('getpid/<uid>', views.getpid),
    path('release/<uid>', views.release),
    path('stop/<uid>', views.stop),
]
