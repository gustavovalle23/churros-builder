import os
import shutil
from slugify import slugify


project_name: str = slugify(input('Project name? (churros-project) ').lower()) or 'churros-project'
project_description: str = input('Project description? (Project generated by churros-cli) ')
project_author_name = input('Project author\'s name? (anonymous) ')
project_license: str = input('What license do you want to use? (MIT, BSD or GNU) ').upper()
rest_layer = input('Add rest layer? (Y/n) ')

f"""
    Your Churros project has been created! 🌿
    Are you ready to unlock your domain? 

    Next steps:

    $ cd {project_name}
    $ python3 -m venv venv
	$ source venv/bin/activate
	$ pip3 install -r requirements.txt
	$ python main.py

"""

run_now = input('Run it now? ')
if os.path.exists(project_name):
	shutil.rmtree(project_name)

os.system(f'mkdir {project_name}')
os.system(f'cp install-requirements.sh {project_name}')
os.chdir(f'./{project_name}')
os.system('python3 -m venv venv')
os.system('bash ./install-requirements.sh')
