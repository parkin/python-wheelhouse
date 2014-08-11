#python-wheelhouse#
[![Build Status](https://travis-ci.org/parkin/python-wheelhouse.svg?branch=master)](https://travis-ci.org/parkin/python-wheelhouse)

Small collection of Python [wheels](http://wheel.readthedocs.org/en/latest/). See the collection [here](https://parkin.github.io/python-wheelhouse/).

#Built on Ubuntu 12.04#

PySide (python 2.7)
PySide (python 3.4)

tables (python 2.7)

##PySide##

Built a PySide [wheel](http://wheel.readthedocs.org/en/latest/) so Travis-CI builds using Python3.4 do not have to build PySide from source.

Following these [instructions](http://pyside.readthedocs.org/en/latest/building/linux.html), I built a PySide wheel by:

    $ git clone https://github.com/PySide/pyside-setup.git pyside-setup
    $ cd pyside-setup
    $ python3.4 setup.py bdist_wheel --qmake=/usr/bin/qmake-qt4 --version=1.2.2
    
The wheel is hosted at https://github.com/parkin/travis-python3.4-PySide-wheel.

##Usage##
In your .travis.yml file, include the following:

    install:
      - sudo apt-get install libqt4-dev
      - pip install --find-links https://parkin.github.io/python-wheelhouse/ --use-wheel PySide;
      # Travis CI servers use virtualenvs, so we need to finish the install by the following
      - python ~/virtualenv/python${TRAVIS_PYTHON_VERSION}/bin/pyside_postinstall.py -install

