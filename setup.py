from setuptools import setup, find_packages
import patl

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="Patl",
    version=patl.version,
    author="Ajay Patil",
    author_email="ajay.patil.a01@gmail.com",
    description="Patl helps you in creating a monitorable structure for your files and folder of your big project.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ajay1290/patl",
    license='MIT License',
    packages=find_packages(),
    entry_points = {
        'console_scripts': ['patl=patl.commands:main'],
    }
)

