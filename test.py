import PySide
print('Imported PySide version: ' + PySide.__version__)
# PySide might not be linked to Shiboken correctly, this will check that it is.
from PySide import QtGui
print('Imported PySide.QtGui')
