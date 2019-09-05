import os

import eventlet
import requests
import socketio
from django.http import HttpResponse

from apps.chat_bot.serializers import ThreadSerializer, ChatBotSerializer
from apps.chat_bot.views import chat_bot

async_mode = 'eventlet'

basedir = os.path.dirname(os.path.realpath(__file__))
sio = socketio.Server(async_mode=async_mode)
thread = None


def index(request):
    global thread
    if thread is None:
        thread = sio.start_background_task(background_thread)
    return HttpResponse(open(os.path.join(basedir, 'static/index.html')))


def background_thread():
    """Example of how to send server generated events to clients."""
    count = 0
    while True:
        sio.sleep(10)
        count += 1
        sio.emit('my response', {'data': 'Server generated event'},
                 namespace='/chat')

@sio.on('my event', namespace='/chat')
def test_message(sid, message):
    serializer = ThreadSerializer(data=message)
    if serializer.is_valid():
        instance = serializer.save()
    sio.emit('my response user', {'thread_id': ThreadSerializer(instance).data, 'user_name': str(instance)}, room=sid,
             namespace='/chat')


@sio.on('my question event', namespace='/chat')
def test_broadcast_message(sid, message):
    data = chat_bot(question=message['question'], thread_id=message['thread_id'])
    sio.emit('robot answer event', {'data': data}, namespace='/chat')


@sio.on('join', namespace='/chat')
def join(sid, message):
    sio.enter_room(sid, message['room'], namespace='/chat')
    sio.emit('my response', {'data': 'Entered room: ' + message['room']},
             room=sid, namespace='/chat')


@sio.on('leave', namespace='/chat')
def leave(sid, message):
    sio.leave_room(sid, message['room'], namespace='/chat')
    sio.emit('my response', {'data': 'Left room: ' + message['room']},
             room=sid, namespace='/chat')


@sio.on('close room', namespace='/chat')
def close(sid, message):
    sio.emit('my response',
             {'data': 'Room ' + message['room'] + ' is closing.'},
             room=message['room'], namespace='/chat')
    sio.close_room(message['room'], namespace='/chat')


@sio.on('my room event', namespace='/chat')
def send_room_message(sid, message):
    sio.emit('my response', {'data': message['data']}, room=message['room'],
             namespace='/chat')


@sio.on('disconnect request', namespace='/chat')
def disconnect_request(sid):
    sio.disconnect(sid, namespace='/chat')


@sio.on('connect', namespace='/chat')
def test_connect(sid, environ):
    sio.emit('my response', {'data': 'Connected', 'count': 0}, room=sid,
             namespace='/chat')


@sio.on('disconnect', namespace='/chat')
def test_disconnect(sid):
    print('Client disconnected')
