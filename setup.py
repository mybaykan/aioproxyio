
from setuptools import setup

def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name='aioproxyio',
    version='0.0.1',
    description='Asyncrhonous wrapper for proxycheck.io API',
    author='Mert Yakup Baykan',
    author_email='mertbaykan007@gmail.com',
    license='Apache License 2.0',
    install_requires=get_requirements(),
    packages=['aioproxyio'],
    zip_safe=False
)
