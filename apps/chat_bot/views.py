from rest_framework import mixins, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.chat_bot.models import Threads
from apps.chat_bot.pair import pairs
from apps.chat_bot.serializers import ChatBotSerializer, ThreadSerializer


def checkKey(dict, key):
    if key in dict.keys():
        return dict[key]
    else:
        return False


class ChatBotApiView(APIView):
    serializer_class = ChatBotSerializer

    """
    This APIView for REST API
    :url' http://localhost/api/ or http://127.0.0.1:8000/api/
    """

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            question = request.data['question']
            thread_id = request.data['thread_id']
            if question == 'hi':
                thread = Threads.objects.get(id=thread_id)
                respective = checkKey(pairs, question)
                if respective:
                    return Response({'result': '{} {}'.format(respective, thread.user_name)}, status=status.HTTP_200_OK)
            respective = checkKey(pairs, question)
            if respective:
                return Response({'result': respective}, status=status.HTTP_200_OK)
            else:
                return Response({'result': "sorry, I don't understand you"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def chat_bot(question, thread_id):
    """
    for socket io
    :url http://localhost/chat or http://127.0.0.1:8000/chat/
    :param question:
    :param thread_id:
    :return:
    """
    question = question.lower()
    if question == 'hi':
        thread = Threads.objects.get(id=thread_id)
        respective = checkKey(pairs, question)
        if respective:
            return '{} {}'.format(respective, thread.user_name)
    respective = checkKey(pairs, question)
    if respective:
        return respective
    else:
        return "sorry, I don't understand you"


class ThreadViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    serializer_class = ThreadSerializer
    http_method_names = ('post',)

    def get_serializer(self):
        return self.serializer_class()

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            thread = serializer.save()
            return Response({'result': ThreadSerializer(thread).data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
