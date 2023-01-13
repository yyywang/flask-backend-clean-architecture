# -*- coding: utf-8 -*-
"""
  Created by 怀月 on 2023/1/12.
"""

__all__ = ['setting']

import os

from . import development, production

setting_dict = {
    "development": lambda: development,
    "production": lambda: production
}

current_evn = os.environ.get("APP_ENV") or "development"
setting = setting_dict.get(current_evn)()

del development
del production

print("current_flask_server_env = %s " % current_evn)
