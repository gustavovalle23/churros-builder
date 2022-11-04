from datetime import datetime


class User:
    id: int
    name: str
    email: str
    password: str
    active: bool
    created_at: datetime


class Order:
    id: int
    name_of_product: str
    avaiable_qtd: int
