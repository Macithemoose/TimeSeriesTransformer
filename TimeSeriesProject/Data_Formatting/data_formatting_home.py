import numpy as np
import io
import os
import matplotlib.pyplot as plt

snip10_fasd = np.load('C:/Users/Annah/Documents/dev/maci/TimeSeriesTransformer/FASD_data/fasd_data/snip10_fasd_rawdata.npy', allow_pickle=True)
snip10_control = np.load('C:/Users/Annah/Documents/dev/maci/TimeSeriesTransformer/FASD_data/control_data/snip10_control_rawdata.npy', allow_pickle=True)

num_people_fasd = snip10_fasd.shape[0]
num_people_control = snip10_control.shape[0]

snip10_master = []
fasd_label = [1]
control_label = [0]

#handling FASD:
for person in range(num_people_fasd):
  try:
    h_saccade = snip10_fasd[person][0][:,0]
    h_saccade = np.append(h_saccade,fasd_label) #add a label (1 for fasd)
    snip10_master.append(h_saccade)
  except Exception as e:
    print(f'for fasd: an error occurred with person {person}: {e}')

#handling control:
for person in range(num_people_control):
  try:
    h_saccade = snip10_control[person][0][:,0]
    h_saccade = np.append(h_saccade,control_label) #append a label (0 for control)
    snip10_master.append(h_saccade)
  except Exception as e:
    print(f'for control: an error occurred with person {person}: {e}')

snip10_master = np.array(snip10_master)
print(snip10_master.shape)
#part that won't work:
# for person in range(num_people_fasd):
#     print(person)
#     if person!=17 and person!=20:
#       h_saccade = snip10_fasd[person][0][:,0]
#       snip1_master.append(h_saccade)
#     else:
#        continue

