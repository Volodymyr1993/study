from setuptools import setup, find_packages

__version__ = '0.0.1'

setup(
    name='study',
    description='My study',
    version=__version__,

    python_requires='>=3.8.7',

    install_requires=[
        'allure-pytest',
        'playwright',
        'flask',
        'requests'
    ],

    tests_require=[
        'pytest',
        'pytest-playwright',
    ],

    packages=find_packages(),
)
