import numpy as np
import pandas as pd
import io
import os
import matplotlib.pyplot as plt

snip10_fasd = np.load('C:/Users/Annah/Documents/dev/maci/TimeSeriesTransformer/FASD_data/fasd_data/snip10_fasd_rawdata.npy', allow_pickle=True)
snip10_control = np.load('C:/Users/Annah/Documents/dev/maci/TimeSeriesTransformer/FASD_data/control_data/snip10_control_rawdata.npy', allow_pickle=True)

num_people_fasd = snip10_fasd.shape[0]
num_people_control = snip10_control.shape[0]

snip10_train = []
snip10_test = []
fasd_label = [1]
control_label = [0]

#handling FASD:
for person in range(num_people_fasd):
  if person < 5 or person > (num_people_fasd - 5):
    try:
      h_saccade = snip10_fasd[person][0][:,0]
      h_saccade = np.append(h_saccade,fasd_label) #append a label (0 for control)
      snip10_test.append(h_saccade)
    except Exception as e:
      print(f'for fasd: an error occurred with person {person}: {e}')
  else:
    try:
      h_saccade = snip10_fasd[person][0][:,0]
      h_saccade = np.append(h_saccade,fasd_label) #append a label (0 for control)
      snip10_train.append(h_saccade)
    except Exception as e:
      print(f'for fasd: an error occurred with person {person}: {e}')
#handling control:
for person in range(num_people_control):
  if person < 5 or person > (num_people_control - 5):
    try:
      h_saccade = snip10_control[person][0][:,0]
      h_saccade = np.append(h_saccade,control_label) #append a label (0 for control)
      snip10_test.append(h_saccade)
    except Exception as e:
      print(f'for control: an error occurred with person {person}: {e}')
  else:
    try:
      h_saccade = snip10_control[person][0][:,0]
      h_saccade = np.append(h_saccade,control_label) #append a label (0 for control)
      snip10_train.append(h_saccade)
    except Exception as e:
      print(f'for control: an error occurred with person {person}: {e}')
snip10_train = np.array(snip10_train)
snip10_test = np.array(snip10_test)
df = pd.DataFrame(snip10_train)
df = pd.DataFrame(snip10_test)
df.to_csv("C:/Users/Annah/Documents/dev/maci/TimeSeriesTransformer/FASD_data/snip10_train.csv",header=False)
df.to_csv("C:/Users/Annah/Documents/dev/maci/TimeSeriesTransformer/FASD_data/snip10_test.csv",header=False)
print(snip10_train.shape)
print(snip10_test.shape)


