import setuptools
from os import sys
import pypandoc

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

long_description = pypandoc.convert_file('README.md', 'rst')
long_description = long_description.replace("\r", "")

setuptools.setup(
    name="site-map-parser",
    version="0.3.0",
    author="Dave O'Connor",
    author_email="github@dead-pixels.org",
    description="Script/Library to read and parse sitemap.xml data",
    long_description=long_description,
    url="https://github.com/daveoconnor/site-map-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=['smapper'],
    include_package_data=True,
    package_data={
        '': ['*.ini'],
    },
    python_requires='>=3.5',
    tests_require=["pytest"],
    setup_requires=[] + pytest_runner,

)
