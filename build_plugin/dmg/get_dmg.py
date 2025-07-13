# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/7/12 18:57
@Author   : wieszheng
@Software : PyCharm
"""

import os
import sys

app_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(app_dir)

from build_plugin.config import Config


appName = Config.appName  # 应用名称
appVersion = Config.appVersion  # 应用版本号

dmgName = f'{appName}-{appVersion}_macOS'


# 获取配置文件内容
def get_json():
    return """filename = '""" + dmgName + """'
volume_name = '""" + dmgName + """.dmg'
format = 'UDBZ'
files = ['""" + app_dir + r"""/build/""" + appName + """.app']
symlinks = {'Applications': '/Applications'}
icon_locations = {
    '""" + appName + """.app': (160, 120),
    'Applications': (430, 120),
}
window_rect = ((200, 200), (590, 416))
icon_size = 60
text_size = 12
badge_icon = '""" + app_dir + r"""/static/app.icns'
"""


# 生成配置文件
json_dir = os.path.dirname(__file__)
with open(os.path.join(json_dir, 'dmg.py'), 'w+', encoding='utf-8') as f:
    f.write(get_json())
