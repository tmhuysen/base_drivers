#!/usr/bin/env python
import os
import subprocess
import sys
import numpy as np
from scipy.interpolate import interp1d

distance = sys.argv[1]
interval = float(sys.argv[2])
basis_set = sys.argv[3]
file_name = sys.argv[4]
out_name = sys.argv[5]



x = 0
if len(sys.argv) > 5:
    x = sys.argv[5]


file = open(file_name, "r")
data = file.read()


def newlined_tabbed_data_string_to_dataset(string, define_type = None):

    string_list = string.strip("\n").split("\n")
    index = 0
    is_start_correct = True
    if define_type is not None:
        while is_start_correct:
            try:
                x = string_list[index].split("\t")
                for t in x:
                    define_type(t)
                is_start_correct = False
            except ValueError:
                index += 1
    line_length = len(string_list[index].split("\t"))
    total_set = list()
    for i in range(line_length):
        total_set.append(list())
    for j in range(index, len(string_list)):
        line = string_list[j]
        split_line = line.strip("\n").split("\t")

        for i in range(line_length):
            if define_type is None:
                total_set[i].append(split_line[i])
            else:

                total_set[i].append(define_type(split_line[i]))
    return tuple(total_set)


def array_to_csl(array):
    s = ''.join([str(el) + "," for el in array])
    return s[:-1]

data_sets = newlined_tabbed_data_string_to_dataset(data, float)

cargsstr = array_to_csl(data_sets[1])
pathx = os.environ['PEXE1']
pathy = "davidson_constrained_N_O"
print(pathx)
pathexe = os.path.join(pathx,pathy)
print("-----------------")
print(pathexe)
print("-----------------")

subprocess.run((pathexe, "-d", distance, "-s", basis_set, "-c", cargsstr,"-x",str(x), "-e", out_name))
