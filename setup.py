import os 
from typing import List 
from setuptools import setup,find_packages 

# This function will read dependencies and packages required for project from requirements.txt file.
def get_requirements()->List[str]: 
    requirements_list:List[str]=[]
    try: 
        with open("requirements.txt","r")as file: 
            lines=file.readlines()
            for line in lines: 
                requirements=line.strip()
                if requirements and requirements != "-e .": 
                    requirements_list.append(requirements)
    
    except FileNotFoundError: 
        print("requirements.txt not found !")
    
    return requirements_list 

# Setup configuration for the package
setup(
    version="0.0.1", 
    author="Mayur", 
    packages=find_packages(),           # Automatically finds all Python packages
    install_requires=get_requirements() # Installs dependencies from requirements.txt
)