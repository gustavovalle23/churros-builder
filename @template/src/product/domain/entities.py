# -*- coding: utf-8 -*-
from typing import Optional
from datetime import datetime, timezone
from dataclasses import dataclass
from datetime import datetime
from src.user.domain.entities import User

from src.__seedwork.domain.entities import Entity


@dataclass(kw_only=True, frozen=True, slots=True)
class Product(Entity):
    id: int
    name: str
    valid_date: datetime
    user: User
    quantity: Optional[int] = 10
    weight: Optional[float] = 0.0
    description: Optional[str] = 'no description'
    active: Optional[bool] = False

    def __post_init__(self):
        if not self.created_at:
            self._set('created_at',  datetime.now(
                timezone.utc))
