# serializers.py
from rest_framework import serializers
from .models import Projects , Postproject, Team,Coumunity, Postteam # 올바른 import

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class PostProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postproject
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class CoumunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Coumunity
        fields = '__all__'

class PostteamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postteam
        fields = '__all__'
