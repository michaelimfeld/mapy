#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="mapy",
    version="0.00.01",
    license="MIT",
    description="simple tool to manage custom cs:go maps on your server",
    author="Michael Imfeld",
    author_email="michaelimfeld@crooked.ch",
    maintainer="Michael Imfeld",
    maintainer_email="michaelimfeld@crooked.ch",
    platforms=["Linux", "Windows", "MAC OS X"],
    url="https://github.com/michaelimfeld/mapy",
    packages=["mapy"],
    install_requires=["pycurl"],
    data_files=[('/etc/', ['mapy/mapy.conf'])],
    entry_points={"console_scripts": ["mapy = mapy.main:main"]},
    classifiers=[
      "Development Status :: 4 - Beta",
      "Environment :: Console",
      "Intended Audience :: Developers",
      "Intended Audience :: Education",
      "Intended Audience :: Other Audience",
      "Natural Language :: English",
      "Operating System :: MacOS :: MacOS X",
      "Operating System :: OS Independent",
      "Operating System :: Microsoft :: Windows",
      "Operating System :: Microsoft :: Windows :: Windows 7",
      "Operating System :: Microsoft :: Windows :: Windows XP",
      "Operating System :: POSIX",
      "Operating System :: POSIX :: Linux",
      "Programming Language :: Python",
      "Programming Language :: Python :: 2.6",
      "Programming Language :: Python :: 2.7",
      "Programming Language :: Python :: 3",
      "Programming Language :: Python :: 3.2",
      "Programming Language :: Python :: Implementation",
      "Topic :: Education :: Testing",
      "Topic :: Software Development",
      "Topic :: Software Development :: Testing"
      ]
    )

