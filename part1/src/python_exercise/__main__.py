import argparse

def is_palindrome(name):
    '''
    Check if a given name is palindrome

    Args:
        name: string
    '''
    letters = list(name)
    letters.reverse()
    return name == ''.join(letters)


def validate_palidrome(name):
    '''
    Validates if a given name is palindrome
    and prints the result in the console

    Args:
        name: string
    '''
    print(f'Palindrome: {is_palindrome(name)}')


parser = argparse.ArgumentParser(
    description='Thank you for asking for help. These tools are used to generate a Django project and convert CloudFormation code from YAML to JSON.',
    prog='python_exercise',
)

parser.add_argument(
    '-cp', '--check-palindrome',
    help='Use this flag to check if the name of the project is palindrome (default: %(default)s)',
    dest='check_palindrome',
    default=True,
    action='store_true'
)

parser.add_argument('project_name', help='The project name')

options = parser.parse_args()

if options.check_palindrome:
    validate_palidrome(options.project_name)


# print(options)



