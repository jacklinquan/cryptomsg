from setuptools import setup

setup(
    name="cryptomsg",
    version="0.1.0",
    description="A simple python package to encrypt and decrypt messages " \
        + "with AES CBC mode.",
    long_description="https://github.com/jacklinquan/cryptomsg",
    long_description_content_type="text/markdown",
    url="https://github.com/jacklinquan/cryptomsg",
    author="Quan Lin",
    author_email="jacklinquan@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3"
    ],
    packages=["cryptomsg"],
    install_requires=["pyaes"]
)
