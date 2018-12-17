#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author    : Young
@Email     : hyc554@outlook.com
@site      : http://www.cnblogs.com/huang-yc/
@File      : my_tasks.py
@version   : 1.0
@Time      : 2018/12/12 17:48
Description about this file: 

"""


from django_celery_beat.models import PeriodicTask  #倒入插件model
from rest_framework import serializers
from rest_framework import pagination
from rest_framework.viewsets import ModelViewSet
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodicTask
        fields = '__all__'

class Mypagination(pagination.PageNumberPagination):
    """自定义分页"""
    page_size=2
    page_query_param = 'p'
    page_size_query_param='size'
    max_page_size=4

class TaskView(ModelViewSet):
    queryset = PeriodicTask.objects.all()
    serializer_class = Userserializer
    permission_classes = []
    pagination_class = Mypagination
