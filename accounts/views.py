from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # No middleware here because anyone can sign up
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer
