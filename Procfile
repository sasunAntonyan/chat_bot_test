release: ./scripts/release-tasks.sh
socket: python manage.py run_socket
web: gunicorn chat_bot.wsgi -k eventlet