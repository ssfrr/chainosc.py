#!/usr/bin/env python

from setuptools import setup


setup(
    name='chainosc',
    version='0.0.1',
    description="A simple OSC server that pulls data from the Chain API",
    #long_description=LONG_DESC,
    author='Spencer Russell',
    author_email='sfr@mit.edu',
    #url=URL,
    license='MIT',
    scripts=['chainosc'],
    #test_suite='skeleton.tests',
    install_requires=[
        'chainclient>=0.1',
        'websocket-client',
        'pyliblo',
        'coloredlogs'
    ],
)
