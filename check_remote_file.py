#!/usr/bin/python

import subprocess
import pipes
import os
import getpass

## Ask for .flv to search for
print "Please enter a .flv to search for"

detected = False
wowza_server = ['first_server', 'second_server']
filepath = '/tmp/'
filename = raw_input()
for server in wowza_server:
    resp = subprocess.call(
        ['ssh', getpass.getuser()+'@'+server, 'test -e ' + pipes.quote(filepath + filename)])
    if resp == 0:
        print ('%s exists on %s' % (filepath + filename, server))
        detected = filepath + filename
    else:
        print "No match found on %s" % (server)

# Error checking
print "detected path is =" + detected

if detected is False:
    quit()

## Shall we download the FLV?
print "Would you like to download this file?"

if raw_input() == 'yes':
    os.system('scp %s .' %(detected))
