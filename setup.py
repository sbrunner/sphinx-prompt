# -*- coding: utf-8 -*-

import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = (
    open(os.path.join(here, 'README.rst')).read()
)

install_requires = [
    'Sphinx',
    'pygments',
]
setup_requires = [
]
tests_require = [
]

setup(
    name='sphinx-prompt',
    version='0.2.1',
    description="""
Sphinx directive to add unselectable prompt
""",
    long_description=README,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
    ],
    author='Stéphane Brunner',
    author_email='stephane.brunner@camptocamp.com',
    url='http://github.com/sbrunner/sphinx-prompt',
    license='BSD',
    keywords='gis tilecloud chain',
    packages=find_packages(exclude=["*.tests", "*.tests.*"]),
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
)
