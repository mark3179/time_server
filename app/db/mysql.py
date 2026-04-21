from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.config import settings

# engine 负责数据库连接与连接池管理。
engine = create_engine(
    settings.mysql_url,
    pool_pre_ping=True,
)

# SessionLocal 是会话工厂，每次调用都会创建一个独立 Session。
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db() -> Generator[Session, None, None]:
    # FastAPI 依赖：每个请求分配一个 Session，并在结束后自动关闭。
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()