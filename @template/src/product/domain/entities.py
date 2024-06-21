# -*- coding: utf-8 -*-
from typing import Optional
from datetime import datetime, timezone
from dataclasses import dataclass
from datetime import datetime, timezone
from src.user.domain.entities import User

from src.__seedwork.domain.entities import Entity


@dataclass(kw_only=True, frozen=True, slots=True)
class Product(Entity):
    id: int
    name: str
    expiration_date: 'Datetime'
    user: 'User'
    quantity: int = 10
    weight: float = 0.0
    description: str = 'no description'
    active: bool = False

    def __post_init__(self):
        if not self.created_at:
            self._set('created_at', datetime.now(timezone.utc))
