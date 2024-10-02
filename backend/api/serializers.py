from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для Task."""

    class Meta:
        """Метаданные для сериализатора Task."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
