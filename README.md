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
## Entity generator
With types supported:
- [x] str
- [x] int
- [x] bool
- [x] float
- [x] datetime
- [ ] decimal
- [ ] Other entity


## SqlAlchemy Model Generator
With types supported:
- [ ] str
- [ ] int
- [ ] bool
- [ ] float
- [ ] datetime
- [ ] decimal
- [ ] Other entity

To test it, run:
```bash
python code_generator.py
```


Currently supported technologies are:
## Database:
- PostgreSQL

## Back-end Framework: MySQL
- FastAPI

## APIs Layers:
- Rest
