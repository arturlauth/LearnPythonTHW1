try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools

config = {
    'description': 'My Project',
    'author': 'Artur Henrique Lauth',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'arturlauthmain@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['lexicon'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
