from django.contrib import admin
from django.urls import path, include
from student import views
from rest_framework import routers

# router = routers.DefaultRouter(trailing_slash=False)
# router.register('images', views.showImages)

urlpatterns = [
path('', views.getRoutes),
path('images/', views.showImages),
path('upload/', views.uploadFile, name='upload_file'),
]