
from rest_framework import serializers

from apps.chat_bot.models import Threads


class ChatBotSerializer(serializers.Serializer):
    question = serializers.CharField(allow_blank=False)
    thread_id = serializers.CharField(allow_blank=False, allow_null=False)


class ThreadSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(allow_null=False, allow_blank=False, write_only=True)
    thread_id = serializers.ReadOnlyField(source='get_thread_id')

    class Meta:
        model = Threads
        fields = [
            'user_name',
            'thread_id',
        ]
