import os
import subprocess
import sys

import numpy as np

distance = sys.argv[1]
input_range = float(sys.argv[2])
interval = float(sys.argv[3])
basis_set = sys.argv[4]

cargs = np.arange(-input_range, input_range, interval)

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

subprocess.run((pathexe, "-d", distance, "-s", basis_set, "-c", cargsstr, "-e", "cluster"))
