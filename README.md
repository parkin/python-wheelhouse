travis-python3.4-PySide-wheel
==================================

Built a PySide [wheel](http://wheel.readthedocs.org/en/latest/) so Travis-CI builds using Python3.4 do not have to build PySide from source.

Following these [instructions](http://pyside.readthedocs.org/en/latest/building/linux.html), I built a PySide wheel by:

    $ git clone https://github.com/PySide/pyside-setup.git pyside-setup
    $ cd pyside-setup
    $ python3.4 setup.py bdist_wheel --qmake=/usr/bin/qmake-qt4 --version=1.2.2
    
The wheel is hosted at https://github.com/parkin/travis-python3.4-PySide-wheel.

Note on my machine with Ubuntu 14.04, this created the file `dist/PySide-1.2.2-cp34-cp34m-linux_x86_64.whl` which was roughly 17 MB. When I instead included the `--standalone` tag in the build step, the file was ~77 MB.

Note that as of yet, only `import PySide` has been tested. Due to this being built under Ubuntu 14.04 and Travis-Ci servers running Ubuntu 12.04, I do not know how functional the PySide library is. If you run into problems, you may want to redo this on a machine running Ubuntu 12.04.

Usage
=====
In your .travis.yml file, include the following:

    install:
      - sudo apt-get install libqt4-dev
      - pip install --find-links https://parkin.github.io/travis-python3.4-PySide-wheel/ --use-wheel PySide;
