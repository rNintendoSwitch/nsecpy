from setuptools import find_packages, setup

setup(
    name='nsecpy',
    packages=find_packages(include=['nsecpy']),
    version='0.0.0',
    description='',
    author='7bitlyrus',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)