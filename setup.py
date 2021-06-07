from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='fractional',
  version='0.0.1',
  description='A library that helps to get fractional part of a number',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Suyog Savalkar',
  author_email='suyog231002@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='fraction', 
  packages=find_packages(),
  install_requires=[''] 
)