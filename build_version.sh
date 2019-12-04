rm -rf build dist pyplan.egg-info
python setup.py build
python3 setup.py sdist bdist_wheel