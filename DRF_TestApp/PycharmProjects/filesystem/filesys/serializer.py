from django.contrib.auth.models import User
from rest_framework import serializers
from filesys.models import Filepath

class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filepath
        fields = ('id', 'name', 'parent')
