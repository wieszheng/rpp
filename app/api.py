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


@router.get("/dd")
async def read_root():
    return {"message": "Hello World"}