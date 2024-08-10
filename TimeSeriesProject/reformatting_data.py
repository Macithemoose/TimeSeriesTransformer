import numpy as np
import io
import os
import matplotlib.pyplot as plt

snip1_fasd = np.load('/lab/mksimmon/Downloads/TimeSeriesProject/fasd_data/fasd_data/snip1/fasd_rawdata.npy', allow_pickle=True)
snip1_control = np.load('/lab/mksimmon/Downloads/TimeSeriesProject/fasd_data/control_data/snip1/control_rawdata.npy', allow_pickle=True)

num_people_fasd = snip1_fasd.shape[0]
num_people_control = snip1_control.shape[0]

snip1_master = []

#part that works:
h_saccade = snip1_fasd[17][0][:,0]
print(h_saccade.shape)
snip1_master.append(h_saccade)
print(snip1_master)

snip1_master = []

#part that won't work:
for person in range(num_people_fasd):
    print(person)
    h_saccade = snip1_fasd[person][0][:,0]
    snip1_master.append(h_saccade)

# print(num_people_control)
# print(num_people_fasd)
