from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'tasks', views.TaskViewSet, basename='task')


urlpatterns = [
    path("", views.api_root),
    path("", include(router.urls))
]
