from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class LoginUser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response({'message':'ok'})



class InfoUser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        return Response(
            {
                'email': request.user.email,
                'username': request.user.username,
                'name': request.user.name,
            }
        )