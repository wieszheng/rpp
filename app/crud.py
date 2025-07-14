# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/7/13 14:31
@Author   : wieszheng
@Software : PyCharm
"""
from sqlalchemy_crud_plus import CRUDPlus

from app.models import Task, MonitorData

task_crud = CRUDPlus(Task)
data_crud = CRUDPlus(MonitorData)