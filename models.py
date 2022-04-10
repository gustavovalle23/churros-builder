import dataclasses
from datetime import datetime
from typing import List, Dict
import inspect
from sqlalchemy.orm import declarative_base
from fastapi import FastAPI



def generate_methods(attributes: Dict[str, type]):
    with open('repositories.py', 'w') as f:
        for key, value in attributes.items():
            field = key
            type_field = value.__name__


            f.write(f"""
def get_{field}() -> {type_field}:
    return 1

""")


def model(class_call) -> object:
    def check(
        *args, **kwargs
    ) -> None:
        print(inspect.getmembers(class_call)[0][1])
        generate_methods(inspect.getmembers(class_call)[0][1])
    return check



@model
class Profile:
    profile_name: str
    ProfileName: str
    birth_date: datetime



class User:
    first_name: str
    last_name: str
    birth_date: datetime
    profile: List[Profile]


profile = Profile()


# def custom_decorator(func):
#     def wrapper(*args, **kwargs):
#         print('Something is happening before...')
#         func(*args, **kwargs)
#         print('Something is happing after...')
#     return wrapper


# @custom_decorator
# def say_whee(number: int):
#     print('Whee!')


# say_whee(2)
