# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/7/13 14:20
@Author   : wieszheng
@Software : PyCharm
"""
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    基础模型
    """
    __abstract__ = True