import setuptools
from os import sys

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

with open('README.md') as readme:
    long_description = readme.read()

setuptools.setup(
    name="site-map-parser",
    version="0.3.8",
    author="Dave O'Connor",
    author_email="github@dead-pixels.org",
    description="Script/Library to read and parse sitemap.xml data",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daveoconnor/site-map-parser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    scripts=['smapper'],
    include_package_data=True,
    package_data={
        '': ['*.ini'],
    },
    python_requires='>=3.6',
    tests_require=["pytest"],
    setup_requires=[] + pytest_runner,
    install_requires=[
        'lxml',
        'requests',
        'python-dateutil',
    ]
)
