import setuptools

with open("DESCRIPTION.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='colotext',
    version='1.0.0.dev1',
    author="Vagner Bessa",
    author_email="bessavagner@gmail.com",
    description="Color you text terminal output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bessavagner/colortext",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
 )
