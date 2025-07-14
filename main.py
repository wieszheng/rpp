# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/7/12 17:09
@Author   : wieszheng
@Software : PyCharm
"""
import os
import threading
from contextlib import asynccontextmanager

import uvicorn
import webview
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from app import api
from app.db import setup_database


@asynccontextmanager
async def lifespan(_: FastAPI):
    """
    用于在启动时初始化数据库
    :param _: FastAPI
    :return:
    """
    await setup_database()
    yield


app = FastAPI(
    title="Test Automation API",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

app.include_router(api.router)


def get_unused_port():
    """
    获取一个未被占用的端口
    :return:
    """
    import socket
    import random
    while True:
        port = random.randint(1024, 65535)  # 端口范围一般为1024-65535
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind(("localhost", port))
            sock.close()
            return port
        except OSError:
            pass


def main():
    """
    主函数
    :return:
    """
    port = get_unused_port()
    t = threading.Thread(target=uvicorn.run, args=(app,), kwargs={"port": port})
    t.daemon = True
    t.start()

    screens = webview.screens
    screens = screens[0]
    width = screens.width
    height = screens.height
    init_width, init_height = int(width * 2 / 3), int(height * 4 / 5.5)
    min_width, min_height = int(width / 2), int(height / 2)

    webview.create_window(title="RPP v1.0.01", url="web/index.html", width=init_width, height=init_height,
                          min_size=(min_width, min_height))
    webview.start(debug=True, http_server=True)


if __name__ == '__main__':
    main()
    # uvicorn.run(app, host="127.0.0.1", port=8000)
