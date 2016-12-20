#!/usr/bin/python
#passenger_wsgi.py
import sys, os
# Path for the Python interpreter to use
from config import INTERP

if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
    #Should resume execution from the top of the file

from api import app

application = app
