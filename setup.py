# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

install_requires = [
    "Sphinx",
    "pygments",
]
setup_requires = []
tests_require = []

setup(
    name="sphinx-prompt",
    version="1.4.0",
    description="Sphinx directive to add unselectable prompt",
    long_description="`Sphinx directive to add unselectable prompt <https://github.com/sbrunner/sphinx-prompt>`_",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
    ],
    author="Stéphane Brunner",
    author_email="stephane.brunner@camptocamp.com",
    url="https://github.com/sbrunner/sphinx-prompt",
    license="BSD",
    keywords="gis tilecloud chain",
    packages=find_packages(exclude=["*.tests", "*.tests.*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
)
