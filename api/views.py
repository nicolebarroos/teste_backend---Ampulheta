from django.contrib.auth.hashers import check_password
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from api.models import User, Time, Project
from api.serializers import UserSerializer, TimeSerializer, ProjectSerializer


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=['POST'], permission_classes=[IsAuthenticated], detail=False)
    def create_user(self, request):
        password = request.data['password']
        username = request.data['username']
        email = request.data['email']

        try:

            user = User.objects.create_user(username=username, password=password, email=email)
            serializer = UserSerializer(user)
            return Response({'user': serializer.data}, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({'message': 'Fail to create user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(methods=['POST'], permission_classes=[AllowAny], detail=False)
    def authenticate(self, request):
        username = request.data['username']
        password = request.data['password']

        try:
            user = User.objects.get(username=username)
            success = check_password(password, user.password)
            if success:
                token = Token.objects.get_or_create(user=user)
                serializer = UserSerializer(user)
                return Response({'token': token[0].__str__(), 'user': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'User or password invalid'}, status=status.HTTP_400_BAD_REQUEST)

        except ObjectDoesNotExist:
            return Response({'message': 'User not registered in the system'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'message': 'Fail to create user'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class TimeViewSet(ModelViewSet):
    queryset = Time.objects.all()
    serializer_class = TimeSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=['GET'], permission_classes=[IsAuthenticated], detail=False)
    def get_time_by_project(self, request):
        id_project = request.query_params['id_project']
        try:
            times = Time.objects.filter(project_id=id_project)
            serializer = TimeSerializer(times, many=True)
            return Response({'times': serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'message': 'Fail to get time by project'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

