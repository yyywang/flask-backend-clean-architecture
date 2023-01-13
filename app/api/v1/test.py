# -*- coding: utf-8 -*-
"""
  Created by 怀月 on 2023/1/12.
"""
from app.utils.redprint import Redprint

test_api = Redprint('test')


@test_api.route('')
def hello():
    return 'test ok'
