try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = {
    'description': 'My Project',
    'author': 'Artur Henrique Lauth',
    'url': 'link do git',
    'download_url': 'Where to download it.',
    'author_email': 'arturlauthmain@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'Project_1'
}

setup(**config)
