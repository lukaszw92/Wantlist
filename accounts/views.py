from django.shortcuts import render
from rest_framework.views import APIView

from accounts.serializers import UserSerializer
from rest_framework.response import Response
from .models import User


class UserListView(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)