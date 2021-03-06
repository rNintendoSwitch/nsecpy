from setuptools import find_packages, setup


setup(
    name='nsecpy',
    packages=find_packages(include=['nsecpy']),
    version='0.4.0',
    description='Python library that provides common interfaces to select Nintendo eShop APIs',
    author='7bitlyrus, mralext20',
    license='MIT',
    install_requires=['dateparser', 'aiohttp'],
)
