import numpy as np
import pandas as pd
import io
import os
import matplotlib.pyplot as plt


def snipToCSV(snip):
  snip_fasd = np.load(f'/lab/mksimmon/Downloads/TimeSeriesTransformer/FASD_data/fasd_data/snip{snip}_fasd_rawdata.npy', allow_pickle=True)
  snip_control = np.load(f'/lab/mksimmon/Downloads/TimeSeriesTransformer/FASD_data/control_data/snip{snip}_control_rawdata.npy', allow_pickle=True)
  num_people_fasd = snip_fasd.shape[0]
  num_people_control = snip_control.shape[0]
  snip_master = []
  fasd_label = [1]
  control_label = [0]


  #handling FASD:
  for person in range(num_people_fasd):
    try:
      h_saccade = snip_fasd[person][0][:,0]
      h_saccade = np.append(h_saccade,fasd_label) #add a label (1 for fasd)
      snip_master.append(h_saccade)
    except Exception as e:
      print(f'for fasd snip {snip}: an error occurred with person {person}: {e}')

  #handling control:
  for person in range(num_people_control):
    try:
      h_saccade = snip_control[person][0][:,0]
      h_saccade = np.append(h_saccade,control_label) #append a label (0 for control)
      snip_master.append(h_saccade)
    except Exception as e:
      print(f'for control snip {snip}: an error occurred with person {person}: {e}')

  snip_master = np.array(snip_master)
  df = pd.DataFrame(snip_master)
  df.to_csv(f"/lab/mksimmon/Downloads/TimeSeriesTransformer/FASD_data/snip{snip}_master.csv",header=False)
  print(snip_master.shape)


snipToCSV(2)