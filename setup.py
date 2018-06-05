import pathlib
from setuptools import find_packages, setup

import versioneer

NAME = "eps_entropy"
DESCRIPTION = ""
URL = "https://github.com/ohjeah"
EMAIL = "info@markusqua.de"
AUTHOR = "Markus Quade"
PYTHON = ">=3.6"

here = pathlib.Path(__file__).parent

with open(here / "requirements.txt", "r") as f:
    REQUIRED = f.readlines()

setup(
    name=NAME,
    version=versioneer.get_version(),
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=["test", "bench"]),
    include_package_data=True,
    install_requires=REQUIRED,
    python_requires=PYTHON,
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.6",
    ],
    cmdclass=versioneer.get_cmdclass()
)
