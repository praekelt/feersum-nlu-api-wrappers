# coding: utf-8

"""
    FeersumNLU API

    This is the HTTP API for Feersum NLU. See https://github.com/praekelt/feersum-nlu-api-wrappers for examples of how to use the API.  # noqa: E501

    OpenAPI spec version: 2.0
    Contact: nlu@feersum.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "feersum_nlu"
VERSION = "2.0.34.post3"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="FeersumNLU API",
    long_description=open("README.rst", "r").read() + "\n\n" + open("CHANGELOG.rst", "r").read(),
    author="Feersum Engine",
    author_email="nlu@feersum.io",
    url="https://github.com/praekelt/feersum-nlu-api-wrappers",
    download_url='https://github.com/praekelt/feersum-nlu-api-wrappers/archive/' + VERSION + '.tar.gz',
    keywords=["Feersum", "NLU", "NLP"],
    classifiers=[],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True
)
