#!/usr/bin/python

import os
import subprocess
import sys

#file = sys.argv[1]
#name =  ".tmp"
newname = "tmp"

print newname
#change = 'cp sys.argv[1] sys.argv[1].auto'
#subprocess.call(["ls", file, newname])
subprocess.call(["ls -ltr | wc > newname"])
#subprocess.call(["mv", newname, file])
