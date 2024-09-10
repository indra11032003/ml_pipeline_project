from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath: str) -> List[str]:
    """
    This function will return the list of requirements
    by reading the requirements.txt file.
    """
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        # Remove new line characters from each requirement
        requirements = [i.replace("\n", "") for i in requirements]

        # Remove '-e .' from the requirements if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements


setup(
    name="ml_project",  # Replace with your project name
    version="0.1.0",
    author="Indrajit Patil",
    author_email="indrajitp746@gmail.com",
    description="A machine learning project training",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
    url="https://github.com/indra11032003/ml_pipeline_project.git"
)
