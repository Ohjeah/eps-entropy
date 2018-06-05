import os
from setuptools import find_packages, setup

# import versioneer

NAME = "eps_entropy"
DESCRIPTION = ""
URL = "https://gl.ambrosys.de/mq/potboiler"
EMAIL = "info@markusqua.de"
AUTHOR = "Markus Quade"
VERSION = "0.0.0"

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, "requirements.txt"), "r") as f:
    REQUIRED = f.readlines()


setup(
    name=NAME,
    #version=versioneer.get_version(),
    version=VERSION,
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=["test", "bench"]),
    include_package_data=True,
    install_requires=REQUIRED,
    # license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3.6",
    ],
    # cmdclass=versioneer.get_cmdclass()
)
