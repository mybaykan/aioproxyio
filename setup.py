
from setuptools import setup

def get_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name='aioproxyio',
<<<<<<< HEAD
    version='0.0.2',
=======
    version='0.0.1',
>>>>>>> 8f2ad302dd49dea8551aed0adb8bad174159d249
    description='Asynchronous wrapper for proxycheck.io API',
    author='Mert Yakup Baykan',
    author_email='mertbaykan007@gmail.com',
    license='Apache License 2.0',
    install_requires=get_requirements(),
    packages=['aioproxyio'],
    zip_safe=False
)
