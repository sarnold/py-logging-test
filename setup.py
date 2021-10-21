import setuptools

# Get a long description from the README file
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="py-logging-test",
    version="0.0.1",
    author="Steve Arnold",
    author_email="nerdboy@gentoo.org",
    description="Python package template logging test",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarnold/py-logging-test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
)
