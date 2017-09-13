import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django_header_auth',
    version='0.1-dev',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='A simple Django app to manage remote authenticated consumers as users.',
    long_description=README,
    url='https://www.paiuolo.it',
    author='Luca Bertuol',
    author_email='paiuolo@gmail.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    install_requires=[
          'Django>=1.11',
          'djangorestframework',
    ],
    test_suite='django_header_auth.runtests.runtests'
)
