#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="maccas",
    version="0.0.1",
    description="PyTorch Lightning Project Setup - computer vision",
    author="",
    author_email="",
    url="https://github.com/user/project",
    install_requires=["lightning", "hydra-core"],
    packages=find_packages(),
    # use this to customize global commands available in the terminal after installing the package
    entry_points={
        "console_scripts": [
            "maccas_train = maccas.train:main",
    #        "maccas_eval = maccas.eval:main",
        ]
    },
)