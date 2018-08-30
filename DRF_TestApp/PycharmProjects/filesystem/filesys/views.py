# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from filesys .models import Filepath
from .serializer import PathSerializer
# Create your views here.
class PathViewSet(viewsets.ModelViewSet):
    queryset = Filepath.objects.all()
    serializer_class = PathSerializer