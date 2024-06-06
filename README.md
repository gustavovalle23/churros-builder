# Churrospy

Library that unify all core librarys from churrospy

### Installing
Obs: it is very recommend you use a virtual environment

```sh
# Create a virtual env
python3 -m venv venv

# Activate the virtual env
source venv/bin/activate

# Install dependencies inside virtual env
pip3 install -r requirements.txt

# To exit the virtual env you could execute the following command
deactivate
```

# Currently features available:
- [x] application (dtos, errors and routers)
- [x] domain (entities)
- [x] infra (models, database config and repositories)

## Entity generator
With types supported:
- [x] str
- [x] int
- [x] bool
- [x] float
- [x] datetime
- [ ] decimal
- [x] Other entity
- [x] default value



Some other features:
- [x] default value
- [x] multiple entities
- [x] Seedworks

## SqlAlchemy Model Generator
With types supported:
- [x] str
- [x] int
- [x] bool
- [x] float
- [x] datetime
- [ ] decimal
- [ ] Other entity

Some other features:
- [x] default value
- [x] multiple models

Crud Available:
- [x] Find all (with pagination)
- [x] find by id (unique)
- [ ] find by field (each field)
- [x] create
- [x] update
- [ ] inactivate
- [x] delete
- [x] convert model to entity
- [ ] automated tests


FastAPI features:
- [ ] Response Models


To test it, run:
```bash
python server.py
```
or
```bash
python mock_server.py
```

Currently supported technologies are:
## Database:
- [x] Sqlite3
- [ ] PostgreSQL
- [ ] MySQL
- [ ] MongoDB

## Back-end Framework:
- [x] FastAPI
- [ ] Flask
- [ ] Django (maybe)

## APIs Layers:
- [x] Rest
- [ ] GraphQL


To run generated application:
```bash
uvicorn src.main:app --reload
```


## Todo
- [x] Fix seedwork error: missing UniqueEntityId
    - Removed. Let user add a id itself
- [ ] Fix ModuleNotFoundError: No module named 'src'
- [x] Fix duplicate imports
- [x] Fix duplicate models structure
- [ ] sqlalchemy.exc.InvalidRequestError: Table 'products' is already defined for this MetaData instance.  Specify 'extend_existing=True' to redefine options and columns on an existing Table object.
- [ ] sqlalchemy.exc.CompileError: (in table 'products', column 'user'): Can't generate DDL for NullType(); did you forget to specify a type on this Column?


## Testing

Request body example:
```json
[
 {
  "name": "product",
    "items": [
      {
        "name": "name",
        "type": "str", 
        "default_value": "General Product" 
      }
    ]
  }
]
```