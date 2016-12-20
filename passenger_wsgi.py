#!/usr/bin/python
#passenger_wsgi.py

import sys, os

# Path for the Python interpreter to use
INTERP = '/usr/bin/python'
# First argument to execl is the path to the binary, the second is arg0,
# which is again the path to the binary, then the rest of the arguments

def _get_log():
    return file('/home/andrew/Documents/GitHub/Gemapi-v0/passengerwsgi.log', 'a')

log = _get_log()
print >>log, "Running %s" % (sys.executable)

if sys.executable != INTERP:
    print >>log, "Detected wrong interpreter location, swapping to %s" % (INTERP)
    #swapping interpreters will not flush any files
    log.flush()
    log.close()
    os.execl(INTERP, INTERP, *sys.argv)
    #Should resume execution from the top of the file
else:
    print >>log, "Correct interpreter location"

log.flush()
log.close()

from api import app

application = app
