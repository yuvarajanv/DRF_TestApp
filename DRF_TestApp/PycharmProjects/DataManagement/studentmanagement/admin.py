# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Question
from .models import Question_q
from .models import Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Question_q)
admin.site.register(Choice)