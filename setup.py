from setuptools import setup

setup(
    name='quora',
    version='1.0',
    description='Python package which parses Quora.',
    author='Tapasweni Pathak',
    author_email='tapaswenipathak@gmail.com',
    url='https://github.com/tapaswenipathak/quora',
    packages=['quora'],
    install_requires=[
        "beautifulsoup",
        "qtopic"
    ]
    )

