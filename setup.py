from setuptools import find_packages,setup
from typing import List

hyphen_e_dot = '-e .'

def get_requirements(file_path) ->list[str]:
    '''
    this function will return the list of requirements
    
    :param file_path: requirements.txt file path
    :return: list of libraries mentioned in requirements.txt
    :rtype: list[str]
    
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','') for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(
    name='MLProject',
    version='0.0.1',
    author='Guna Shekar Reddy Avula',
    author_email='gunashekar9327@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),

)