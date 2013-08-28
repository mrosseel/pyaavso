import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='pyaavso',
    version=__import__('pyaavso').__version__,
    description='A Python library for working with AAVSO data.',
    long_description=read('README.rst'),
    author='Zbigniew Siciarz',
    author_email='zbigniew@siciarz.net',
    url='http://github.com/zsiciarz/pyaavso',
    download_url='http://pypi.python.org/pypi/pyaavso',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    classifiers=['Development Status :: 1 - Planning',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python',
                 'Topic :: Scientific/Engineering :: Astronomy',
                 'Topic :: Utilities'],
)