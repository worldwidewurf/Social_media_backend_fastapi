from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
"""_summary_: This module contains the database configuration. the login credentials are stored in the .env file to avoid hardcoding them.

Yields:
    _type_: sqlalchemy.engine.base.Engine
"""
SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
def get_db():
    """returns a database session

    Yields:
        _type_: sqlalchemy.orm.session.Session
    """
    db = session_local()
    try:
        yield db
    finally:
        db.close()
