from setuptools import setup

with open("readme.md", "r",encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    description="A small package for dvc ml pipeline.",
    author="PinnOps",
    long_description=long_description,
    url="https://github.com/Abhinav003/dvc-ml-tensorflow-demo",
    packages=["src"],
    install_requires=["dvc",
        "pandas",
        "numpy",
        "pyYAML",
        "matplotlib",
        "tensorflow",
        "boto3",
        "botocore"],
    python_requires=">3.7"
)