from rest_framework import serializers

from api.models import User, Project, Time


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class TimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Time
        fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        extra_kwargs = {
            'users': {'required': False},
            'times': {'required': False},
        }
        fields = ('title', 'description', 'users', 'times')

