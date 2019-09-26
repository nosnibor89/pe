import argparse

from python_exercise.tools.aws.cf_manager import CFManager
from python_exercise.tools.palindrome import validate_palidrome
from python_exercise.tools.scaffold import django

parser = argparse.ArgumentParser(
    description='''
    Thank you for asking for help. 
    These tools are used to generate a Django project and convert CloudFormation code from YAML to JSON.
    ''',
    prog='python_exercise',
)

parser.add_argument(
    '-cp', '--check-palindrome',
    help='Use this flag to check if the name of the project is palindrome (default: %(default)s)',
    dest='check_palindrome',
    default=True,
    action='store_true'
)

parser.add_argument(
    '-cf', '--convert-cf',
    help='Use this flag to transform a CF yaml file to json. We\'ll use the name of the project',
    dest='cf_file',
)

parser.add_argument(
    '-sdp', '--scaffold-django-project',
    help='Use this flag to indicate you want to scaffold a django project in the provided path',
    dest='django_project_path',
)

parser.add_argument('project_name', help='The project name')

options = parser.parse_args()

if options.check_palindrome:
    validate_palidrome(options.project_name)

if options.cf_file:
    manager = CFManager(options.cf_file)
    manager.dump_json(target=options.project_name)

if options.django_project_path:
    django.create_project(options.project_name)

# print(options)
