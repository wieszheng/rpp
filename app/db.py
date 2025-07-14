# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Version  : Python 3.12
@Time     : 2025/7/13 14:21
@Author   : wieszheng
@Software : PyCharm
"""

from typing import AsyncGenerator
from sqlalchemy import URL
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from app.models import Base

url = URL.create(
    drivername="mysql+aiomysql",
    username="root",
    password="mysql123",
    host="82.157.176.120",
    port=3306,
    database="test",
    query={"charset": "utf8mb4"},
)
_async_engine = create_async_engine(url, future=True, echo=False)
_async_db_session = async_sessionmaker(bind=_async_engine, class_=AsyncSession, autocommit=False, expire_on_commit=False)


async def setup_database():
    """Set up the test database."""
    async with _async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def async_db_session() -> AsyncGenerator[AsyncSession, None]:
    """
    创建新的数据库会话.
    :return:
    """
    async with _async_db_session() as session:
        yield session
