from django.contrib import admin
from django.urls import path
from app import views
from .views import TodoList, TodoDetails
urlpatterns = [
    path("todo/", TodoList.as_view()),
    path("todo/<int:id>/", TodoDetails.as_view())
    
]
