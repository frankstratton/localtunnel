#!/usr/bin/env python
import os
from setuptools import setup, find_packages

from localtunnel import __version__

setup(
    name='localtunnel',
    version='0.6.4beta',
    author='Jeff Lindsay',
    author_email='progrium@gmail.com',
    description='Magically expose a local port to the Internet',
    license='MIT',
    classifiers=[
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
    url="http://github.com/progrium/localtunnel",
    packages=find_packages(),
    install_requires=['eventlet', 'requests', 'argparse', 'yunomi'],
    data_files=[],
    dependency_links = [
        'https://github.com/progrium/yunomi/tarball/master#egg=yunomi'
    ],
    entry_points={
        'console_scripts': [
            'localtunnel-beta = localtunnel.client:run',
            'localtunneld = localtunnel.server.cli:run',]},
)
