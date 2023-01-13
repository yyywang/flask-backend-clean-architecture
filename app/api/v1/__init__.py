# -*- coding: utf-8 -*-
"""
  Created by 怀月 on 2023/1/12.
"""
from flask import Blueprint


def create_v1() -> Blueprint:
    bp_v1 = Blueprint("api/v1", __name__)

    from .test import test_api

    test_api.register(bp_v1)

    return bp_v1
