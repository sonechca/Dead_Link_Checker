import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Dead-Link-Checker",
    version="1.0.0",
    author="Mintae Kim",
    author_email="mkim221@myseneca.ca",
    description="The command line tool for checking dead link",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sonechca/Dead_Link_Checker",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "requests == 2.24.0",
        "datetime == 4.3",
        "colorama == 0.4.4",
        "black == 20.8b1",
        "flake8 == 3.8.4",
        "pre-commit == 2.7.1",
        "pytest == 6.1.2",
        "pytest-cov == 2.10.1",
    ],
    entry_points={
        "console_scripts": [
            "DLChecker = src.DLChecker:main_wrapper",
        ]
    },
    python_requires=">=3.6",
)