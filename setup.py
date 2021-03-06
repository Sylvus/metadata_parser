from setuptools import setup, find_packages
import os, re

# store version in the init.py
with open(
        os.path.join(
            os.path.dirname(__file__),
            'metadata_parser', '__init__.py')) as v_file:
    VERSION = re.compile(
        r".*__VERSION__ = '(.*?)'",
        re.S).match(v_file.read()).group(1)

# go
setup(name='metadata_parser',
      version=VERSION,
      description="A module to parse metadata out of documents",
      long_description=open("README.rst").read() + "\n",
      classifiers=[
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Topic :: Text Processing :: Markup :: HTML',
          'Topic :: Software Development :: Libraries :: Python Modules',
      ],
      keywords='opengraph protocol facebook',
      author='Jonathan Vanasco',
      author_email='jonathan@findmeon.com',
      url='https://github.com/jvanasco/metadata_parser',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'tests']),
      test_suite='tests',
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'BeautifulSoup4',
          'requests>=1.2'
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
