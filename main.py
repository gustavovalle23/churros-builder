from code_generator.models_example import  User, Order
from code_generator.domain.entities import generate_entities
from code_generator.infra.models import generate_models
from code_generator.infra.repositories import generate_repository
from code_generator.application import generate_routers, generate_dtos


generate_entities([User, Order])
generate_models([User, Order])
generate_repository(User)
generate_repository(Order)
generate_routers(User)
generate_routers(Order)
generate_dtos(User)
generate_dtos(Order)
