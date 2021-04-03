import site
import sys

from setuptools import find_packages, setup

site.ENABLE_USER_SITE = "--user" in sys.argv

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
        "Development Status :: 5 - Production/Stable",
        "Environment :: Plugins",
        "Environment :: Web Environment",
        "Framework :: Sphinx :: Extension",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Documentation :: Sphinx",
        "Topic :: Documentation",
        "Topic :: Software Development :: Documentation",
    ],
    author="Stéphane Brunner",
    author_email="stephane.brunner@camptocamp.com",
    url="https://github.com/sbrunner/sphinx-prompt",
    license="BSD",
    keywords="sphinx shell prompt",
    packages=find_packages(exclude=["*.tests", "*.tests.*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
)
