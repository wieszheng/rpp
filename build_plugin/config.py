# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/7/12 18:57
@Author   : wieszheng
@Software : PyCharm
"""

import os
import platform
import sys


class Config:

    # 程序基础配置信息
    appName = 'RPP'  # 应用名称
    appNameEN = 'RPP'  # 应用名称-英文（用于生成缓存文件夹，必须是英文）
    appVersion = "V1.0.01"  # 应用版本号
    appDeveloper = "wieszheng"  # 应用开发者
    appBlogs = "https://wieszheng.github.io/code-docs/"  # 个人博客
    appPackage = 'vip.rpp.com'  # 应用包名，用于在本地电脑生成 vip.pangao.ppx 唯一文件夹
    appUpdateUrl = 'https://wieszheng.github.io/code-docs/'  # 获取程序更新信息 https://api.github.com/repos/pangao1990/ppx/releases/latest
    appISSID = '317D500E-96FC-ED71-06D4-2D6C94794DD8'  # Inno Setup 打包唯一编号。在执行 pnpm run init 之前，请设置为空，程序会自动生成唯一编号，生成后请勿修改！！！

    # 系统配置信息（不需要修改，可以自动获取）
    cpuArch = platform.processor()  # 本机CPU架构
    appSystem = platform.system()  # 本机系统类型
    appIsMacOS = appSystem == 'Darwin'  # 是否为macOS系统
    codeDir = sys.path[0].replace('base_library.zip',
                                  '')  # 代码根目录，一般情况下，也是程序所在的绝对目录（但在build:pure打包成的独立exe程序中，codeDir是执行代码的缓存根目录，而非程序所在的绝对目录）
    staticDir = os.path.join(codeDir, 'static')  # 代码根目录下的static文件夹的绝对路径
    appDataDir = ''  # 电脑上可持久使用的隐藏目录
    downloadDir = ''  # 电脑上的下载目录

    # 其他配置信息
    devPort = '5173'  # 开发环境中的前端页面端口
    devEnv = True  # 是否为开发环境，不需要手动更改，在程序运行的时候自动判断
    ifCoverDB = False  # 是否覆盖电脑上存储的数据库，默认不覆盖。只有在变更数据库密码或者数据库改动非常大，不得已的情况下才建议覆盖数据库
    typeDB = 'json'  # 数据库类型，目前支持: json, sql
    pwDB = b'XnDRG0k1Q7hz-FxOyIRlGnUlRS6kTaUq_6ZwJbirkwY='  # 数据库密码，typeDB=json时有效。若要重置密码，请在执行 pnpm run init 之前，设置为空，程序会自动生成密码，生成后请勿修改！！！

