from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool, QueuePool

_connection_pool = None


def get_connection_string(read_only: bool = False) -> str:
    """
    Construct the DB URL instead of relying on the string in alembic.ini
    :return: Postgres URL
    """
    return "postgresql+asyncpg://localhost:5432/fastapitest"

# def create_engine() -> AsyncEngine:
#     # pytest-asyncio creates a new event loop per test. Connection pooling with asyncpg does not work with multiple
#     # event loops: https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#using-multiple-asyncio-event-loops
#     # so if the environment is local or test, disable the connection pool.
#     #
#     # QueuePool is the default connection pool and will be used for dev, staging, and production.
#     engine_params = {"future": True, "pool_pre_ping": True, "echo": True, "echo_pool": 'debug'}  # type: Dict[str, Any]
#     if ENV in ("local", "test"):
#         engine_params["poolclass"] = NullPool
#     else:
#         engine_params["poolclass"] = QueuePool
#         engine_params["pool_size"] = db_config["pool"]["min_size"].get(20)
#         engine_params["max_overflow"] = 0
#
#     return create_async_engine(get_connection_string(True), **engine_params)


_engine = create_async_engine(get_connection_string(),
                              future=True,
                              pool_pre_ping=True,
                              echo=True,
                              echo_pool='debug',
                              pool_size=5,
                              max_overflow=0)
async_session = sessionmaker(_engine, expire_on_commit=False, class_=AsyncSession)