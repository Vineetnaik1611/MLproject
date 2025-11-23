# Convert entire project into a package 

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path: str):
    requirements = []
    with open(file_path) as file_obj:
        for line in file_obj:
            req = line.strip()

            # skip blank lines
            if not req:
                continue

            # THIS removes "-e ." correctly
            if req.startswith("-e"):
                continue

            requirements.append(req)

    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Vineet',
    author_email='vnn28@bath.ac.uk',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)