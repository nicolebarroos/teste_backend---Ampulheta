from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from api.models import User
from api.serializers import UserSerializer


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=['GET'], permission_classes=[IsAuthenticated], detail=False)
    def create_user(self, request):
        login = request.data['login']
        password = request.data['password']
        name = request.data['name']
        email = request.data['email']

        try:
            user = User.objects.create(username=login, password=password, name=name, email=email)
            serializer = UserSerializer(user)
            return Response({'user': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': 'Fail to create user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['GET'], permission_classes=[AllowAny], detail=False)
    def authenticate(self, request):
        login = request.data['login']
        password = request.data['password']

        try:
            user = User.objects.get(username=login, password=password)
            token = Token.objects.get_or_create(user=user)
            serializer = UserSerializer(user)
            return Response({'token': token[0].__str__(), 'user': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': 'Fail to create user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)






