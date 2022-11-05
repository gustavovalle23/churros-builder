template_model = """
from datetime import datetime
from sqlalchemy.sql import func
from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Boolean, DateTime, Float, Integer

envs = dotenv_values(".env")
engine = create_engine(envs["DATABASE_URL"])
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
"""

timestamp_model = """
    created_at: datetime = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: datetime = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
    )
"""


imports_entity = """# -*- coding: utf-8 -*-
from uuid import UUID as uuid
from dataclasses import dataclass\n"""



imports_repository = """
# -*- coding: utf-8 -*-
from uuid import uuid1 as uuid
from sqlalchemy.orm import Session, Query
from typing import List
"""