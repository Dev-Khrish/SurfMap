#!/usr/bin/env python3
"""
Setup configuration for SurfMap package.
This file provides backwards compatibility with older setup tools.
Modern Python projects should use pyproject.toml instead.
"""

from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    README = f.read()

setup(
    name="surfmap",
    version="1.2.0",
    description="Advanced Reconnaissance & Analysis Suite for cybersecurity professionals",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Khrish",
    url="https://github.com/dev-Khrish/surfmap",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "surfmap=surfmap.__main__:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security",
    ],
)
