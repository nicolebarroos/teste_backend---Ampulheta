from rest_framework import serializers

from api.models import User, Project, Time


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'password']
        extra_kwargs = {'password': {'required': True, 'min_length': 1}}

    def validate(self, attrs):
        if attrs.password == "":
            raise serializers.ValidationError("Você não pode passar o campo password vazio")
        elif not attrs.password:
            raise serializers.ValidationError("Você não pode passar o campo password nulo")


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

