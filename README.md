# <div align="center"><b><a href="README.md">English</a> | <a href="README_CN.md">简体中文</a></b></div>

# Flask Backend Clean Architecture

A Python Backend Clean Architecture project with Flask, MySQL, JWT Authentication Middleware, Test, and Docker.

## Quick Start

- using docker

```shell
docker-compose --env-file env/.env.dev up
```

- original start

```shell
# custom `DB_CONFIG` in `app/config/development.py` 
pip install -r requirements.txt
flask run
```

## Architecture Layers Of The Project

- Controller
- Views/API
- Model
- Asynchronous task

## Project Folder Structure

```
.
├── app
│   ├── __init__.py
│   ├── api
│   │   └── v1
│   │       ├── __init__.py
│   │       └── test.py
│   ├── config
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   └── views
│       ├── __init__.py
│       └── test.py
├── requiremnets.txt
└── uwsti.py
```

### api

The folder where the api interface code is located.

In practical applications, apis often have version changes. At this time, it is necessary to keep the original api (because it may still be in use) and add a new version of the api. Two or more versions of the api exist at the same time. The URLs of this api should be the same in the RESTful style except for the version number. Directly adding the version number at the end of the URL (for example: V1) can solve this problem, but as the project scale grows, This kind of api will become difficult to maintain. Therefore, split the api version at the project level to improve the maintainability of the project, and implement it based on Blueprint.

After Blueprint is used for api version splitting, more fine-grained api splitting cannot be implemented, such as the auth and test modules under V1. Therefore, Redprint is added to support fine-grained api splitting.

> Reference: 7七月

### config

First of all, you need to know two environments when developing software. One is **development environment**, which means the environment in which the program runs when the programmer develops software (generally personal computer); The second is **production environment**, which means the environment where the program runs after the software is released (the back-end is usually a Linux server).

The development environment is different from the production environment in some configurations, such as database configuration. The test database is used during development, and the production database is used in the production environment. Therefore, the program needs to be connected to the test database during development, and the program needs to be connected to the production database in the production environment. If there is only one configuration, you need to manually modify the database URI for each development to connect the program to the test database, and you need to manually modify the program to connect to the production database when you go online. This manual modification method is troublesome and prone to errors, so use the following method to solve this problem, so that development and production do not need to manually modify the configuration.

Write different configurations of the development environment and the production environment in different files. The development environment is written in `development.py`, and the production environment is written in `production.py`. By setting the environment variable `APP_ ENV` enables the program to choose the configuration of reading from different files at startup. When the program starts, it will read value of `APP_ENV` from the environment variable, if `APP_ ENV==development` it will read the configuration in `development.py`, if `APP_ ENV==production` it will read the configuration in `production.py`, and the specific implementation is [click to view](app/config/__init__. py).

In addition, extract the same configuration of the development environment and the production environment to `base.py`, and import the `base.py` module in `development.py` and `production.py`, which reduces code redundancy.

### views

### models

### utils

### uwsgi
