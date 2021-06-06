from django.urls import path, include
from . import views
from django.db import models

urlpatterns = [
    path('', views.callhome),
    path('info/', views.info),
    path('detail/<str:mdname>', views.detail, name='amd'),
    path('mdinfo/<str:mdname>', views.mdinfo),
    path('detail/', views.one),
    path('mdinfo/', views.one),
    path('newmd/', views.newmd),
    path('detail/<str:mdname>/del', views.delmd, name='dele'),
]
