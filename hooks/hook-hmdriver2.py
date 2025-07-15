# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/7/15 23:35
@Author   : wieszheng
@Software : PyCharm
"""
from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('hmdriver2', includes=['assets'])