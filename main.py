from code_generator.models_example import  User, Order
from code_generator.entities import generate_entities
from code_generator.models import generate_models


generate_entities([User, Order])
generate_models([User, Order])
