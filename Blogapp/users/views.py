from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserModelSerializer

# Create your views here.

class UserView(APIView):
    # and permissions authentication are globally set 
    def get(self, request):

        # a serializer instace for the rquesting user
        Serializer = UserModelSerializer(request.user) 
        return Response(Serializer.data)