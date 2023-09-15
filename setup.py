from setuptools import find_packages,setup
from typing import List


# Added in requirments.txt to trigger setup.py if we particualry install requirements.txt
Hypen_E_Dot='-e .'

# getting modules from requirements.txt 
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if Hypen_E_Dot in requirements:
            requirements.remove(Hypen_E_Dot)

    return requirements

setup(
    name="Diamond Price Prediction",
    version='0.0.1',
    author='Harshit Pathak',
    author_email='hpankur03@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)