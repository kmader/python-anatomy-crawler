try: # for pip >= 10
    from pip._internal.req import parse_requirements
except ImportError: # for pip <= 9.0.3
    from pip.req import parse_requirements
from setuptools import setup
import os

DIR = os.path.dirname(os.path.abspath(__file__))
VERSION = '1.0.0-dev'

setup(
    name='python-anatomy-crawler',
    version=VERSION,
    author='Jan Papousek',
    author_email='jan.papousek@gmail.com',
    url='https://github.com/papousek/python-radiopaedia',
    include_package_data=True,
    packages=[
        'radiopaedia',
        'radiopaedia.commands',
    ],
    install_requires=[
        str(r.req)
        for r in parse_requirements(DIR + '/requirements.txt', session=False)
    ],
    license='MIT',
)
