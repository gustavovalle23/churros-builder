from code_generator.models_example import  User, Order
from code_generator.entities import generate_entities
from code_generator.models import generate_models
from code_generator.repositories import generate_repository
from code_generator.routers import generate_routers


generate_entities([User, Order])
generate_models([User, Order])
generate_repository(User)
generate_repository(Order)
generate_routers(User)
generate_routers(Order)