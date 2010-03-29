import os
from setuptools import setup

# from http://packages.python.org/an_example_pypi_project/setuptools.html
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "plpylint",
    version = "0.1",
    author = "Peter Eisentraut",
    author_email = "peter@eisentraut.org",
    description = ("runs pylint over PostgreSQL PL/Python functions"),
    license = "MIT",
    keywords = "postgresql plpython pylint",
    url = "http://github.com/petere/plpylint",
    scripts = ['plpylint'],
    long_description = read('README'),
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Quality Assurance",
    ],
    install_requires = ['psycopg2'],
)
