from ast import Delete
from django.urls import path
from .views import Add, Get, Delete, Update

urlpatterns = [
    path('add', Add.as_view()),
    path('delete', Delete.as_view()),
    path('update', Update.as_view()),
    path('get', Get.as_view()),
]

