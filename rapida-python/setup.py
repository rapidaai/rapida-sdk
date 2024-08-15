#!/usr/bin/env python
import os.path

from setuptools import find_packages, setup


def read(*parts):
    with open(os.path.join(*parts)) as f:
        return f.read().strip()


classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Programming Language :: Python :: 3.9",
    "Environment :: Web Environment",
    "Intended Audience :: Developers",
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
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    classifiers=classifiers,
    platforms=["POSIX"],
    url="https://github.com/rapidaai/rapida-sdk",
    packages=find_packages(exclude=["examples", "invoker-api.proto"]),
    install_requires=[
        "grpcio==1.65.4",
        "protobuf==5.27.3",
        "pillow==10.4.0"
    ],
    extras_require={
        "grpcio-tools": ["grpcio-tools==1.60.0"],
    },
    tests_require=["pytest", "pytest-cov", "flake8", "black", "mypy"],
    package_data={"rapida-python": ["py.typed"]},
    python_requires=">=3.9",
    include_package_data=True,
)
