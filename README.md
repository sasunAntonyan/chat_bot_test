Chat Bot Development Guide


Development setup

    sudo apt-get install python3-pip
    sudo apt-get install python3-dev python3-setuptools
    sudo apt-get install libpq-dev
    
Create www directory where project sites and environment dir

    mkdir /var/www && mkdir /var/envs && mkdir /var/envs/bin
    
Install virtualenvwrapper

    sudo pip3 install virtualenvwrapper
    sudo pip3 install --upgrade virtualenv
    
Add these to your bashrc virutualenvwrapper work

    export WORKON_HOME=/var/envs
    export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
    export PROJECT_HOME=/var/www
    export VIRTUALENVWRAPPER_HOOK_DIR=/var/envs/bin    
    source /usr/local/bin/virtualenvwrapper.sh
    
Create virtualenv

    cd /var/envs && mkvirtualenv --python=/usr/bin/python3 chat_bot
    
Install requirements for a project.

    cd /var/www/chat_bot && pip install -r requirements.txt
    
    
##Database creation
###For psql

    sudo su - postgres
    psql
    DROP DATABASE IF EXISTS chat_bot;
    CREATE DATABASE chat_bot;
    CREATE USER chat_bot_user WITH password 'dIAWra5UYrXKISYuyJhm1WeWr3kv34QL';
    GRANT ALL privileges ON DATABASE chat_bot TO chat_bot_user;
    ALTER USER chat_bot_user CREATEDB;
    
For Runserver
    python manage.py run_socket