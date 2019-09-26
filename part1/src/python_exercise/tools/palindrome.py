def _is_palindrome(name):
    """
    Check if a given name is palindrome
    :param name: string
    :return:
    """
    letters = list(name)
    letters.reverse()
    return name == ''.join(letters)


def validate_palidrome(name):
    """
    Validates if a given name is palindrome
    and prints the result in the console
    :param name: string
    """
    print(f'Project name is palindrome: {_is_palindrome(name)}')
