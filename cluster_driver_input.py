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
fit = interp1d(data_sets[2], data_sets[1])

start_pop = data_sets[2][0]
end_pop = data_sets[2][-1]


n_ofinputs = int((start_pop-end_pop)/interval)
cargs = np.arange(start_pop, end_pop, interval)
interpolated_input = fit(cargs)
interpolated_input = np.append(interpolated_input, data_sets[1][-1])

print(interpolated_input)


cargsstr = array_to_csl(cargs)
pathx = os.environ['PEXE1']
pathy = "constrained_N_O"
print(pathx)
pathexe = os.path.join(pathx,pathy)
print("-----------------")
print(pathexe)
print("-----------------")

subprocess.run((pathexe, "-d", distance, "-s", basis_set, "-c", cargsstr,"-x","2", "-e", "cluster"))
