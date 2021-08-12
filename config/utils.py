import asyncio
from contextlib import asynccontextmanager
from typing import Any, AsyncGenerator, Dict, List, Optional

from sqlalchemy import Column, text
from sqlalchemy.engine import Row  # type: ignore
# from sqlalchemy.ext.asyncio import AsyncSession
# from sqlalchemy.sql import Select

from .db import async_session


async def execute_query(query: str) -> str:
    # log.info(_engine.sync_engine.pool.status())
    async with async_session() as session:
        return await session.execute(text(query))
