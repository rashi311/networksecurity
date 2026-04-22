'''
It is essitial part of packaging and distribution of python projects.
It is used by setuptools to define the configuration of you projects ,such as metatdata dependencies and more.
'''

from setuptools import find_packages,setup
from typing import List


def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open("requirements.txt","r") as file:
            #read lines from the file
            lines=file.readlines()
            #proces each line
            for line in lines:
                requirement=line.strip()
                ## ignore empty lines and -e .
                if requirement and requirement!= "-e .":
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("My requirements.txt file not found")

    return requirement_lst    

setup(
    name="Network Security",
    version="0.0.1",
    author="Rashi Yadav",
    author_email="rashiy692@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)