from setuptools import find_packages
from setuptools import setup

import os
import sys

# Get the current directory
current_dir = os.path.abspath(os.path.dirname(__file__))

# Add the current directory to the Python path
sys.path.append(current_dir)
'''
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='tiniworld_core',
      version="0.0.5",
      description="A Time-Series Forecasting Project with Facebook Prophet",
      packages=find_packages(),
      install_requires=requirements,
      include_package_data=True,
      #scripts=['scripts/tiniworld_core-run'],
      zip_safe=False)
'''
