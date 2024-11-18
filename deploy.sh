#!/bin/bash
npm install apidoc
pip install virtualenv virtualenvwrapper
mkvirtualenv _ib_env
pip install -r requirements.txt
pip install -r requirements_deploy.txt
DJANGO_SETTINGS_MODULE=smart_food_management.settings."$1" python manage.py build -adj
DJANGO_SETTINGS_MODULE=smart_food_management.settings."$1" python manage.py mocktests
DJANGO_SETTINGS_MODULE=smart_food_management.settings."$1" python manage.py s3push -d --bucket swagger-apidocs --prefix smart_food_management/"$1"
zappa update alpha
zappa manage "migrate --no-input"
