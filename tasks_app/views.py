from rest_framework import generics, permissions, viewsets
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .permissions import IsOwnerOrReadOnly


@api_view()
def api_root(request, format=None):
    return Response({
        'task': reverse('task-list', request=request, format=format),
        'user': reverse('user-list', request=request, format=format)
    })


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



