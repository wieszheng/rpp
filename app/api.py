# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/7/13 14:20
@Author   : wieszheng
@Software : PyCharm
"""

from  fastapi import APIRouter

router = APIRouter()


@router.get("/api/devices")
async def read_root():
    return [{"name": "device1", "id": 1}]



@router.get("/api/scenes")
async def get_scenes():
    return [
        {"id": "scene1", "name": "启动App"},
        {"id": "scene2", "name": "滑动列表"}
    ]