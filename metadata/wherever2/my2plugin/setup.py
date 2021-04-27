from setuptools import setup

setup(
    name='my2plugin',
    version='0.0.1',
    packages=['my2plugin'],
    install_requires=[],
    entry_points={'myapp.plugins': 'b = my2plugin'},
)