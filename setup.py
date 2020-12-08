import os

from semver import VersionInfo
from setuptools import setup, find_packages

# Fail here if the version info is malformed to avoid corrupting our PyPI versions
version = VersionInfo.parse(os.environ['GITHUB_REF'])

setup(name='core-get',
      version=str(version),
      description='Client for the core-get package sharing system',
      url='https://github.com/core-get/core-get',
      author='Oskar Holstensson',
      author_email='oskar@holstensson.se',
      license='MIT',
      install_requires=[
            'tomlkit~=0.7.0',
            'injector~=0.18.3',
            'appdirs~=1.4.4',
            'semver~=2.13.0',
            'requests~=2.25.0',
      ],
      packages=find_packages(),
      zip_safe=False)
