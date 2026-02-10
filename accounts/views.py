from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    # No middleware here because anyone can sign up
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class ProfileView(APIView):
    # This is like Laravel's ->middleware('auth:api')
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # request.user is like Auth::user() in Laravel
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "message": "You are seeing this because you are authenticated!"
        })