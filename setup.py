from setuptools import find_packages, setup


setup(
    name='nsecpy',
    packages=find_packages(include=['nsecpy']),
    version='0.0.0',
    description='Python library that provides common interfaces to select Nintendo eShop APIs',
    author='7bitlyrus',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
)
