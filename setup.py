from setuptools import setup

rel_path = 'README.md'

# python setup.py sdist
setup(name='national-lottery-crawler',
      version='1.0',
      license='MIT',
      description='Ithuba National Lottery Results Crawler',
      long_description="\n" + open(rel_path).read(),
      author='Gert Schreuder',
      url='https://github.com/gertschreuder/national-lottery-crawler',
      packages=['src', 'src.utils', 'src.mappers'],
      entry_points={
          'console_scripts': [ 'src=src.index:main' ]
      },
      install_requires=[ 'selenium==3.141.0' ]
    )

__author__ = 'Gert Schreuder'