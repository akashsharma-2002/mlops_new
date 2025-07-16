#responsible for creating the project as package

from setuptools import find_packages,setup  
#find package actually searched for all __init.__py file present
#in the dierectoyr and based on that it decide which one to trigger for package
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines() 
        """
        this \n is important part as when it takes input from requirements .py file it check each line
        and when going to next line it will print /n also as output so its important 
        that we replace \n with " " .
        """
        requirements=[req.replace("\n","") for req in requirements]

    
        if HYPEN_E_DOT in requirements:
            """ 
            this is used bcoz we are adding a -e . in requirements .txt now this is placed at end of txt file
            bcoz this download the package and trigerrs the setup.py file so its important for -e . to be there
            but it shall not come in our requirement file installation so we remove it from here
            -e = editable
            . = current directory
            """
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='mlops',
version='0.0.1',
author='akash',
author_email='ak@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)