"""Installs a custom package in your Python Environment"""
import os
from setuptools import setup


def read(fname: str) -> str:
    return open(os.path.join(os.path.dirname(__file__), fname), encoding="utf-8").read()


setup(
    name="Dummy module",
    version="0.0.1",
    author="Axel Mendoza",
    author_email="axel.mendoza@epita.fr",
    description="Example description",
    license="BSD",
    packages=['mymodule'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
