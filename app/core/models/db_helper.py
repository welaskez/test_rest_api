from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from core.config import settings


class DatabaseHelper:
    """Simple helper for init/disable db & getting session"""

    def __init__(
        self,
        url: str,
        pool_size: int,
        max_overflow: int,
        echo: bool = False,
        echo_pool: bool = False,
    ) -> None:
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,
        )
        self.session_pool = async_sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False,
            autoflush=False,
            autocommit=False,
        )

    async def dispose(self) -> None:
        await self.engine.dispose()

    async def session_getter(self) -> AsyncSession:
        async with self.session_pool() as session:
            yield session


db_helper = DatabaseHelper(
    url=str(settings.db.url),
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
    echo=settings.db.echo,
    echo_pool=settings.db.echo_pool,
)
