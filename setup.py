from setuptools import setup, find_packages

setup(
    name='paat',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'scikit-learn',
        'flask'
    ],
    entry_points={
        'console_scripts': [
            'paat=paat.cli.main:main',
        ],
    },
    author='Your Name',
    description='Python AI Analysis Tool for static and AI-enhanced security linting',
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
