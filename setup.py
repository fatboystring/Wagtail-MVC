#!/usr/bin/env python
from __future__ import unicode_literals
from wagtail_mvc import __version__
from setuptools import setup, find_packages

setup(
      name='wagtail_mvc',
      version=__version__,
      description='Allows better separation between '
                  'models and views in Wagtail CMS',
      author='Dan Stringer',
      author_email='dan.stringer1983@googlemail.com',
      url='https://github.com/fatboystring/Wagtail-MVC/',
      download_url='https://github.com/fatboystring/Wagtail-MVC/tarball/0.1.0',
      packages=find_packages(exclude=[]),
      license='MIT',
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
      ],
      include_package_data=True,
      keywords=['wagtail', 'django', 'mvc'],
      install_requires=[]
)
