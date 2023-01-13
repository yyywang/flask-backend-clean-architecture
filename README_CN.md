# <div align="center"><b><a href="README.md">English</a> | <a href="README_CN.md">简体中文</a></b></div>

# Flask 后端架构

基于 Flask 的 Python 后端项目架构，包含 MySQL、JWT 鉴权、常用中间件、测试和 Docker 等。

## 项目架构

- Controller
- Views/API
- Model
- Asynchronous task

## 项目文件结构

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

api 接口代码所在的文件夹。

在实际应用中，api 往往会有版本更迭，此时需要保留原有的 api（因为可能还在使用），并增加新版 api，两版或多版 api 同时存在，这种 api 的 URL 在 RESTFul 风格中除了版本号外其余应当都是相同的，直接在 URL 最后加版本号（例如：V1）就可以解决这个问题，但随着项目规模变大，这种 api 会变得难以维护，因此在项目层面做 api 版本拆分，提高项目可维护性，基于 Blueprint 实现。

Blueprint 被用于 api 版本拆分后，更细粒度的 api 拆分便无法实现，例如 V1 版本下的 auth、test 模块，因此增加 Redprint，在 Blueprint 基础上支持更细粒度 api 拆分。

> 参考：7七月

### config

首先需要知晓开发软件时的两种环境，其一是**开发环境**，表示程序员开发软件时程序运行的环境（一般是个人电脑）；其二是**生产环境**，表示将软件发布后，程序运行所处的环境（后端一般是Linux服务器）。

开发环境与生产环境某些配置不同，例如数据库配置，开发时使用测试数据库，在生产环境中使用生产数据库，所以在开发时需要使程序连接测试数据库，在生产环境需要使程序连接生产数据库。假如只有一个配置，那么每次开发都需要手动修改数据库URI，使程序连接到测试数据库，上线时也需要手动修改使程序连接到生产数据库。这种手动修改的方式比较麻烦，而且容易出错，因此使用下面的方式解决这个问题，使开发与生产不需要再手动修改配置。

将开发环境与生产环境不同的配置写在不同的文件，开发环境的写在 `development.py`，生产环境的写在 `production.py`，通过设定环境变量 `APP_ENV` 使程序在启动时选择从不同的文件读取配置。程序启动时会从环境变量读取 `APP_ENV` 的值，如果 `APP_ENV == development` 会读取 `development.py` 中的配置，如果 `APP_ENV == production` 会读取 `production.py` 中的配置，具体实现[点击查看](app/config/__init__.py)。

另外将开发环境与生产环境相同的配置提取到 `base.py`，在 `development.py`，`production.py` 中都导入 `base.py` 模块，这样减少了代码冗余。

### views

### models

### utils

### uwsgi
