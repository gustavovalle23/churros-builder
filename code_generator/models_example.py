from datetime import datetime


class User:
    id: int
    name: str
    email: str
    password: str
    active: bool = False
    birth_date: datetime
    height: float = 1.2


class Order:
    id: int
    name_of_product: str
    avaiable_qtd: int
