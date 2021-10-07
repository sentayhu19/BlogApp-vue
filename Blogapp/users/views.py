from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
# Create your views here.
class UserView(APIView):
    def get (self,request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
