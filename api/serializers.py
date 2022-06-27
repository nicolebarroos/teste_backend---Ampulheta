from rest_framework import serializers

from api.models import User, Project, Time


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name']


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
    users = UserSerializer(read_only=True, required=False)
    times = TimeSerializer(read_only=True, required=False)
    class Meta:
        model = Project
        fields = ['title', 'description', 'users', 'times']

