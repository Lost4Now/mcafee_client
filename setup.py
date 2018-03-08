#!/usr/bin/env python
from setuptools import setup

setup(
    name='mcafee_client',
    version='0.1',
    url='',
    license='MIT',
    author='Lost4Now',
    author_email='david.lord@moesol.com',
    description='McAfee ePolicy Orchestrator API',
    classifiers=[

    ],
    py_modules=['mcafee_client'],
    include_package_data=True,
    zip_safe=True,
    install_requires=['requests']
)
