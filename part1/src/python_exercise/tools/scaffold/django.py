import os
import os.path


def create_project(project_name, path='.'):
    """
    Creates a new django project in the provided path
    :param project_name: string
    :param path: string
    :return: void
    """
    if not os.path.exists(path):
        raise RuntimeError('Incorrect path provided')

    print(f'Creating project skeleton for "{project_name}" project')
    os.system(f'django-admin startproject {project_name} {path}')
