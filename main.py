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
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

from app import api
from app.db import setup_database


@asynccontextmanager
async def lifespan(_: FastAPI):
    await setup_database()
    yield


app = FastAPI(
    title="Test Automation API",
    lifespan=lifespan
)

current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, "view")

app.mount("/view", StaticFiles(directory=static_dir), name="view")


@app.get("/")
async def index():
    return FileResponse(os.path.join(static_dir, "index.html"))


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


def run_server(port: int):
    """
    运行服务器
    :return:
    """

    t = threading.Thread(target=uvicorn.run, args=(app,), kwargs={"port": port})
    t.daemon = True
    t.start()
    print(f"服务器正在运行 http://localhost:{port}")


def web_view_app(port: int):
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

    webview.create_window(title="RPP v1.0.01", url=f"http://127.0.0.1:{port}", width=init_width, height=init_height,
                          min_size=(min_width, min_height))
    webview.start(debug=False)


def main():
    """
    主函数
    :return:
    """
    port = get_unused_port()
    run_server(port)
    web_view_app(port)


if __name__ == '__main__':
    main()
