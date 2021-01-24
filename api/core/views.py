from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated  # <-- Here
from django.contrib.auth.models import User
from api.core.serializers import UserSerializer
# Create your views here.
class HomeView(APIView): 
    permission_classes = (IsAuthenticated,)             # <-- And here
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class UsersView(APIView):
    permission_classes = (IsAuthenticated,)             # <-- And here
    def get(self,request):
        user = User.objects.get(username= request.user);
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def post(self,request):
        serializer =  UserSerializer(data = request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data,status=200)
        else:
            return Response(serializer.errors, status=200)