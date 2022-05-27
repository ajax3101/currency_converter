# Конвертер валют на Django
[![Python Version](https://img.shields.io/badge/python-3.10-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-4.0-brightgreen.svg)](https://djangoproject.com)

Пишем сайт для конвертации валют на Python фреймворке Django, Bootstrap, и отправкой запросов к API с помощью библиотеки requests.

## Running the Project Locally

First, clone the repository to your local machine:
```bash
$ git clone https://github.com/ajax3101/currency_converter.git
$ cd currency_converter/
```
Install the requirements:
```bash
$ python -m venv venv 
$ pip install -r requirements.txt
$ cd app/
$ python manage.py migrate
$ python manage.py runserver
```
