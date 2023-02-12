# -*- coding: utf-8 -*-
"""
  Created by 怀月 on 2023/2/12.
"""
from sqlalchemy import Column, BigInteger, String

from app.models import Base
from app.utils.snowflake import id_generator


class User(Base):
    id = Column(BigInteger, default=id_generator, primary_key=True)
    nickname = Column(String(24), unique=True)
