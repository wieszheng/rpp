# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/7/12 17:09
@Author   : wieszheng
@Software : PyCharm
"""
import webview


def web_view_app():
    """
    webview app
    :return:
    """
    screens = webview.screens
    screens = screens[0]
    width = screens.width
    height = screens.height
    init_width, init_height = int(width * 2 / 3), int(height * 4 / 5.5)
    min_width, min_height = int(width / 2), int(height / 2)

    webview.create_window(title="RPP v1.0.01", url="https://www.baidu.com", width=init_width, height=init_height,
                                   min_size=(min_width, min_height))
    webview.start(debug=False)

if __name__ == '__main__':
    web_view_app()