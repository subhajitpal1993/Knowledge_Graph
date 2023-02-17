import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

with open("requirements.txt") as f:
    required = f.read().splitlines()

setup(
    name="Knowledge_Graph",
    version="0.0.1",
    author="Subhajit Pal",
    author_email="subhajitpal@gmail.com",
    description="Minimalist visual search engine for Knowledge Graph.",
    long_description_content_type="text/markdown",
    license="BSD-3",
    url="https://github.com/subhajitpal1993/Knowledge_Graph",
    package_data={
        "kgsearch": ["web/app.html", "web/style.css", "data/data.csv", "data/metadata.json"]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    python_requires=">=3.7",
    entry_points={
        "console_scripts": ["kg=kgsearch:start"],
    },
)
