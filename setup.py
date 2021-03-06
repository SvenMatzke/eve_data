import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

setup(
    name='django_eve_data',
    version='0.1.3',
    packages=find_packages(),
    include_package_data=True,
    long_description=README,
    url='https://github.com/SvenMatzke/eve_data',
    license='MIT',
    author='Sven Matzke',
    author_email='',
    description='Package for retrieving Data via API or static from Eve Online.',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
