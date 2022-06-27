from rest_framework import serializers

from api.models import User, Project, Time


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(required=False, many=True)
    times = TimeSerializer(required=False, many=True)

    class Meta:
        model = Project
        fields = ['title', 'description', 'users', 'times']