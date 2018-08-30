# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Filepath(models.Model):
    name = models.CharField(max_length=255)
    parent = models.IntegerField()
    #parent = models.ForeignKey('filesys.Filepath', null = True, blank=True)