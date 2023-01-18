from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import ToDoList
from django.contrib.auth.password_validation import validate_password


class TDLSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields=[
            'user',
            'pk',
            'time_created',
            'priority',
            'content'
        ]