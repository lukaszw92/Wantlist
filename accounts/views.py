from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.views import APIView

from accounts.serializers import UserSerializer
from rest_framework.response import Response


class UserListView(APIView):

    def get(self, request):
        users = get_user_model().objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
