#!/usr/bin/env python
import os
import subprocess
import sys

distance = sys.argv[1]
input_range = float(sys.argv[2])
interval = float(sys.argv[3])
basis_set = sys.argv[4]

holycow = int((input_range*2)/interval)
cargs = [-input_range+(x*interval) for x in range(holycow+1)]

def array_to_csl(array):
    s = ''.join([str(el) + "," for el in array])
    return s[:-1]

cargsstr = array_to_csl(cargs)
pathx = os.environ['PEXE1']
pathy = "constrained_N_O"
print(pathx)
pathexe = os.path.join(pathx,pathy)
print("-----------------")
print(pathexe)
print("-----------------")

subprocess.run((pathexe, "-d", distance, "-s", basis_set, "-c", cargsstr,"-x","2", "-e", "cluster"))
