from datetime import datetime


class user:
    id: int
    name: str
    email: str
    password: str
    active: bool
    height: float


class Order:
    id: int
    name_of_product: str
    avaiable_qtd: int
