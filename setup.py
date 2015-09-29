import os
from setuptools import setup



def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "ssphot",
    version = "0.0.1",
    author = "TheOrangeOne",
    platforms = ['Linux'],
    install_requires=['imgurpython'],
    scripts=['ssphot']
    )
