# -*- coding: utf-8 -*-
"""
  Created by 怀月 on 2023/1/12.
"""
from app.models import db, User
from app.utils.fake import fake
from app.utils.redprint import Redprint

test_api = Redprint('test')


@test_api.route('')
def hello():
    return 'test ok'


@test_api.route('/db/user', methods=['GET'])
def get_users():
    users = User.query.all()
    return [user.nickname for user in users]


@test_api.route('/db/user', methods=['POST'])
def create_user():
    nickname = fake.name()
    with db.auto_commit():
        user = User(nickname=nickname)
        db.session.add(user)

    return 'created user: %s' % nickname
