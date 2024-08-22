import numpy as np
import pandas as pd
import io
import os
import matplotlib.pyplot as plt

num_snips = 70

fasd_label = [1]
control_label = [0]

for snip in range(2,num_snips+1):

  snip_fasd = np.load(f'C:/Users/Annah/Documents/dev/maci/TimeSeriesTransformer/FASD_data/fasd_data/snip{snip}_fasd_rawdata.npy', allow_pickle=True)
  snip_control = np.load(f'C:/Users/Annah/Documents/dev/maci/TimeSeriesTransformer/FASD_data/control_data/snip{snip}_control_rawdata.npy', allow_pickle=True)

  num_people_fasd = snip_fasd.shape[0]
  num_people_control = snip_control.shape[0]

  snip_train = []
  snip_test = []

  #handling FASD:
  for person in range(num_people_fasd):
    if person < 5 or person > (num_people_fasd - 5):
      try:
        h_saccade = snip_fasd[person][0][:,0]
        h_saccade = np.append(h_saccade,fasd_label) #append a label (0 for control)
        snip_test.append(h_saccade)
      except Exception as e: pass
        #print(f'for fasd: an error occurred with person {person}: {e}')
    else:
      try:
        h_saccade = snip_fasd[person][0][:,0]
        h_saccade = np.append(h_saccade,fasd_label) #append a label (0 for control)
        snip_train.append(h_saccade)
      except Exception as e: pass
        #print(f'for fasd: an error occurred with person {person}: {e}')
  #handling control:
  for person in range(num_people_control):
    if person < 5 or person > (num_people_control - 5):
      try:
        h_saccade = snip_control[person][0][:,0]
        h_saccade = np.append(h_saccade,control_label) #append a label (0 for control)
        snip_test.append(h_saccade)
      except Exception as e: pass
        #print(f'for control: an error occurred with person {person}: {e}')
    else:
      try:
        h_saccade = snip_control[person][0][:,0]
        h_saccade = np.append(h_saccade,control_label) #append a label (0 for control)
        snip_train.append(h_saccade)
      except Exception as e: pass
        #print(f'for control: an error occurred with person {person}: {e}')
  snip_train = np.array(snip_train)
  snip_test = np.array(snip_test)


  df_train = pd.DataFrame(snip_train)
  df_test = pd.DataFrame(snip_test)

  print(f"training shape for snip {snip} in df: {df_train.shape}")
  print(f"test shape for snip {snip} in df: {df_test.shape}")

  df_train.to_csv(f"C:/Users/Annah/Documents/dev/maci/TimeSeriesTransformer/FASD_data/train/snip{snip}_train.csv",header=False)
  df_test.to_csv(f"C:/Users/Annah/Documents/dev/maci/TimeSeriesTransformer/FASD_data/test/snip{snip}_test.csv",header=False)


