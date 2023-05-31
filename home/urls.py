from django.urls import path
from .views import index, insert_post

urlpatterns = [
    path('', index),
    path("insert", insert_post),
]