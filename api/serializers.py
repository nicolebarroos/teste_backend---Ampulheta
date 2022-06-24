from rest_framework import serializers

from api.models import User, Project, Time


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'
