from rest_framework import serializers

from .models import Todos


class TodosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = [
            'id',
            'Title',
            'Discription',
            'Completed',
        ]
