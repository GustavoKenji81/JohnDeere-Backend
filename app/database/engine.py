from sqlalchemy import create_engine

from app.config.settings import settings


DATABASE_URL = (
    f"mysql+pymysql://"
    f"{settings.db_user}:{settings.db_password}"
    f"@{settings.db_host}:{settings.db_port}"
    f"/{settings.db_name}"
)


engine = create_engine(
    DATABASE_URL,

    pool_pre_ping=True,

    pool_recycle=3600,

    echo=False
)