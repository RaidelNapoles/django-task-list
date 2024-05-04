from django.urls import path
from . import views


urlpatterns = [
    path('task/', views.TaskList.as_view(), name='task-list'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path("", views.api_root),
]
