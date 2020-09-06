from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="python-lib-template-demo",
    description="Demonstrating https://github.com/simonw/python-lib",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/python-lib-template-demo",
    project_urls={
        "Issues": "https://github.com/simonw/python-lib-template-demo/issues",
        "CI": "https://github.com/simonw/python-lib-template-demo/actions",
        "Changelog": "https://github.com/simonw/python-lib-template-demo/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["python_lib_template_demo"],
    install_requires=[],
    extras_require={"test": ["pytest"]},
    tests_require=["python-lib-template-demo[test]"],
)
