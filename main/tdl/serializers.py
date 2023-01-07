from rest_framework import serializers

from .models import ToDoList



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

