from setuptools import setup, find_packages

VERSION = '0.1'
DESCRIPTION = 'My package'
LONG_DESCRIPTION = 'My package with a slightly longer description'

setup(
    name="test_package",
    version=VERSION,
    author="Ankit",
    author_email="karna_ankit@pm.me",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[]
)
