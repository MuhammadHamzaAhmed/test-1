from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from src.server.config import (MYSQL_DB_NAME, MYSQL_HOST, MYSQL_PASSWORD,
                               MYSQL_PORT, MYSQL_USERNAME)

MYSQL_DATABASE_URL = f"mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB_NAME}"
engine = create_engine(MYSQL_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
