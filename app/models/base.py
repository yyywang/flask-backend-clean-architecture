# -*- coding: utf-8 -*-
"""
  Created by 怀月 on 2023/1/19.
"""
from contextlib import contextmanager
from datetime import datetime

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column, SmallInteger, Integer, DATETIME


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as ex:
            db.session.rollback()
            raise ex


class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)


db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    status = Column(SmallInteger, default=1)
    created_date = Column(DATETIME, default=datetime.now)
    modified_date = Column(DATETIME, default=datetime.now, onupdate=datetime.now)

    def set_attrs(self, attrs_dict):
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    def delete(self):
        self.status = 0

    def __getitem__(self, item):
        return getattr(self, item)

    def keys(self):
        """定义序列化时返回的字段"""
        return self.fields

    def hide(self, *keys):
        """定义序列化时隐藏的字段"""
        for key in keys:
            self.fields.remove(key)
        return self

    def append(self, *keys):
        """定义序列化时追加的字段"""
        for key in keys:
            self.fields.apeend(key)
        return self
