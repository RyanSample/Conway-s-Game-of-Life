import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Game-Of-Life", 
    version="0.0.1",
    author="Ryan Sample",
    author_email="sampleryan1@gmail.com",
    description="A python implementation of Conway's 'Game of Life'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RyanSample/Conway-s-Game-of-Life.gitpip",
    packages=setuptools.find_packages(),
    install_requires=[
        'pygame==1.9.6',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)