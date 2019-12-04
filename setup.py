from setuptools import setup
import os

REQ_FILE = os.path.join(os.path.dirname(__file__),
                        'requirements', 'desktop.txt')

required = []
with open(REQ_FILE) as f:
    required = f.read().splitlines()

setup(install_requires=required)
