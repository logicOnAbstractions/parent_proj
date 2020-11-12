from setuptools import setup, find_packages

""" a minimalist setup.py sample structure for a parent proj that uses submodules & manages dependancies smartly"""

setup(
   name='parent_proj',
   version='0.1.0',
   author='Submodule & dependancies managements all in one',
   author_email='francisvachon.it@gmail.com',
   packages=find_packages(where="pysetuptools"),
   scripts=['parent_proj/bin/parent_bash'],
   package_data={'parent_proj':['data/dummy.dat']},
   license='license.txt',
   description='An awesome package that does something',
   long_description=open('readme').read(),
   # install_requires=["pysetuptools"]
)