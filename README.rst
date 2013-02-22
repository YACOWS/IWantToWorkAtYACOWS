test
=====

bootstrap::

    vagrant up
    vagra ssh

    virtualenv venv
    . venv/bin/acticate
    
    cd /vagrant/
    pip install -r requirements.txt

    cd testsite
    ./mange.py syncdb


usage::

    vagrant up
    vagrant ssh

    . venv/bin/activate
    cd /vagrant/testsite

    ./manage.py runserver 0.0.0.0:8000


testing restfull api::

    curl -H "Accept: application/json" http://127.0.0.1:8000/api/v1/poll/

    curl -H "Accept: application/json" http://127.0.0.1:8000/api/v1/choice/