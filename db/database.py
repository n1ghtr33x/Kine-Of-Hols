from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from db.models import Base, User

class Database:
    def __init__(self, db_url):
        self.engine = create_async_engine(db_url, echo=True)
        self.AsyncSessionLocal = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def init_db(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def add_user(self, name: str, password: str, id: str):
        async with self.AsyncSessionLocal() as session:
            result = await session.execute(select(User).where(User.name == name))
            if result.scalars().first():
                return "user exists"
            session.add(User(id=id, name=name, password=password, elixir=5000, money=5000, gems=200))
            await session.commit()
            return "user added"

    async def user_exists_by_id(self, user_id: str) -> bool:
        async with self.AsyncSessionLocal() as session:
            result = await session.execute(select(User).where(User.id == user_id))
            return result.scalars().first() is not None

    async def get_user(self, user_data):
        async with self.AsyncSessionLocal() as session:
            result = await session.execute(select(User).where(User.name == user_data))
            return result.scalars().first()