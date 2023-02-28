from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'body',)

        # serializer has all fields as in models + id
        # can remove fields so it's not displayed to user (i.e. title, body, etc.)
