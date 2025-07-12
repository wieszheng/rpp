# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/7/12 18:57
@Author   : wieszheng
@Software : PyCharm
"""
import random
from pathlib import Path


def get_item(k=4):
    item_list = random.choices(population="0123456789ABCDEF", k=k)
    return "".join(item_list)


def get_app_issid():
    return f"{get_item(8)}-{get_item(4)}-{get_item(4)}-{get_item(4)}-{get_item(12)}"


def run():
    config_path = Path(Path(__file__).absolute().parent.parent.joinpath("config.py"))
    content = ""
    with open(config_path, 'r', encoding='UTF-8') as f:
        content = f.read()

    new_content = content.replace("appISSID = ''", f"appISSID = '{get_app_issid()}'")
    with open(config_path, 'w', encoding='UTF-8') as f:
        f.write(new_content)


if __name__ == '__main__':
    run()
