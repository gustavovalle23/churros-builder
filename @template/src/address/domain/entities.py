from __future__ import annotations
from datetime import datetime, timezone
from typing import Optional
from dataclasses import dataclass
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.__seedwork.domain.entities import Entity


@dataclass(kw_only=True, frozen=True, slots=True)
class Address(Entity):
    id: int
    street: str

    def __post_init__(self):
        if not self.created_at:
            self._set('created_at', datetime.now(timezone.utc))
