# -*- coding: utf-8 -*-
"""
  Created by 怀月 on 2023/1/12.
"""
from app.config.base import *

DEBUG = True

DB_CONFIG = {
    'user': 'root',
    'pwd': 'a12345678',
    'host': 'localhost',
    'port': 3306,
    'db_name': 'fbca'
}

SQLALCHEMY_DATABASE_URI = 'mysql+cymysql://%s:%s@%s:%s/%s?charset=utf8mb4' % (
    DB_CONFIG['user'], DB_CONFIG['pwd'], DB_CONFIG['host'], DB_CONFIG['port'], DB_CONFIG['db_name'])
