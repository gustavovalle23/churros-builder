from datetime import datetime


class User:
    id: int
    name: str
    email: str
    password: str
    active: bool
    birth_date: datetime
    height: float


class Order:
    id: int
    name_of_product: str
    avaiable_qtd: int
