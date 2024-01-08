#!/usr/bin/env python
import os.path

from setuptools import find_packages, setup


def read(*parts):
    with open(os.path.join(*parts)) as f:
        return f.read().strip()


classifiers = [
    "Development Status :: 5 - Development/Unstable",
    "Programming Language :: Python :: 3 :: Only",
    "Environment :: Web Environment",
    "Intended Audience :: RapidaAI Customers",
]

VERSION = {}
# version.py defines VERSION and VERSION_SHORT variables.
# We use exec here to read it so that we don't import scispacy
with open("rapida/version.py") as version_file:
    exec(version_file.read(), VERSION)

setup(
    name="rapida-python",
    version=VERSION["VERSION"],
    author_email="code@rapida.ai",
    description="rapidaAi sdk to integrate rapida.ai api's",
    long_description="\n\n".join((read("README.adoc"), read("CHANGELOG.adoc"))),
    long_description_content_type="text/markdown",
    classifiers=classifiers,
    platforms=["POSIX"],
    url="https://github.com/rapidaai/rapida-sdk",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "aiohttp==3.8.1",
        "grpcio==1.47.0",
        "protobuf==3.20.1",
        "types-protobuf==3.19.22",
        "pydantic==1.9.1",
    ],
    extras_require={
        "grpcio-tools": ["grpcio-tools==1.47.0"],
    },
    tests_require=["pytest", "pytest-cov", "flake8", "black", "mypy"],
    package_data={"rapida-python": ["py.typed"]},
    python_requires=">=3.8",
    include_package_data=True,
)
