try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = {
    'description': 'ex47 project',
    'author': 'Artur Henrique Lauth',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'arturlauthmain@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'ex47'
}

setup(**config)
