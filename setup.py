from setuptools import setup, find_packages

setup(
    name='tymongo',
    version='0.0.4',
    description='A simple MongoDB ORM that support types',
    author='Majid Al-Raimi',
    packages=find_packages(),
    install_requires=[
        'pymongo',
        'pydantic',
        'python-dotenv'
    ],
    license='MIT',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
)