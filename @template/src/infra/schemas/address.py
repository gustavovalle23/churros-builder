
# -*- coding: utf-8 -*-
from datetime import datetime
from sqlalchemy.sql import func
from sqlalchemy import Column, String, Boolean, DateTime, Float, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.infra.models import Base
from src.user.domain.entities import User


class AddressModel(Base):
    __tablename__ = "addresss"

    id: str = Column(String(255), primary_key=True, index=True)
    street: str = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'), unique=True)
    user = relationship('UserModel', back_populates='address')
    created_at: datetime = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at: datetime = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
    )
