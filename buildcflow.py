#!usr/bin/python


import os
import sys



if len(sys.argv) >= 2:
        if sys.argv[1] == "asr9k":

                cmd = "buildx/sestools/ccov " + plat

	elif sys.argv[1] == "ncs6k":

                cmd = "buildx/sestools/cflow " + plat
	else:	
                print("Platform Name provided is not in the Platform List \n")
                sys.exit()
else:
        print("Script is missing the Platform Value \n")

try:
        os.system(cmd)

except RuntimeError:

        print("Buildx Command did not Succeed")

if sys.argv[1] == "ncs6k":

	file = sys.argv[2]

	cflowcmd = "/auto/iox/bin/xr_bld -plat" + plat  + "-jam_opt -d3 -dax -j20 -sCFLOW=" + file + "-l"

	try:
        	os.system(cflowcmd)

	except RuntimeError:

        	print("Cflow build had failed. Pls check the build log file")
~                                                                     
elif sys.argv[1] == "asr9k":

	file = sys.argv[2]

	cflowcmd = "/auto/iox/bin/xr_bld -plat" + asr9k-px  + "-jam_opt -d3 -dax -j20 -sCCOV=" + file + "-l"

	try:
        	os.system(cflowcmd)

	except RuntimeError:

        	print("Cflow build had failed. Pls check the build log file")
