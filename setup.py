# setup.py

from setuptools import setup, find_packages

setup(
    name='my_clock_app',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # No external dependencies in this case, but you might add some
    ],
    entry_points={
        'console_scripts': [
            'clock_app=main:main',  # Adjust as necessary
        ],
    },
)
