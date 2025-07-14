# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/7/13 14:20
@Author   : wieszheng
@Software : PyCharm
"""
from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, Enum, JSON
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    基础模型
    """
    __abstract__ = True


class Task(Base):
    """
    任务模型
    """
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, index=True)
    task_name = Column(String(255), nullable=False)
    app_name = Column(String(255), nullable=False)
    device_id = Column(String(255), nullable=False)
    scene = Column(String(255), nullable=False)
    status = Column(Enum("pending", "running", "completed", "failed"), default="pending")
    create_time = Column(DateTime, nullable=False, default=datetime.now)


class MonitorData(Base):
    """
    监控数据模型
    """
    __tablename__ = "monitor_data"
    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, nullable=False)
    data = Column(JSON, nullable=False)
    create_time = Column(DateTime, nullable=False, default=datetime.now)