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
- [ ] Other entity
- [ ] default value

Some other features:
- [ ] default value
- [x] multiple entities

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
- [ ] default value
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


To test it, run:
```bash
python main.py
```


Currently supported technologies are:
## Database:
- [x] Sqlite3
- [ ] PostgreSQL
- [ ] MySQL
- [ ] MongoDB

## Back-end Framework: MySQL
- [x] FastAPI
- [ ] Flask
- [ ] Django

## APIs Layers:
- [x] Rest
- [ ] GraphQL


To run generated application:
```bash
uvicorn src.main:app --reload
```