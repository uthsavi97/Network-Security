'''
the setup.py file is an essential part of packaging and distributing python projects.It is used by setuptools 
(or distutils in older python versions) to define the configuration of your project,
such as its metadata,dependencies, and more
'''

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    this function will return list of requirements
    
    """
    requirement_lst:List[str]=[]

    try:
        with open('requirements.txt','r') as file:
            #read lines from the file
            lines=file.readlines()
            ## process each line
            for line in lines:
                requirements=line.strip()
                ## ignore empty lines and -e.
                if requirements and requirements!= '-e.':
                    requirement_lst.append(requirements)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirement_lst

setup(
    name="Network-Security",
    version="0.0.1",
    author="uthsavi97",
    author_email="uthsaviyp@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)