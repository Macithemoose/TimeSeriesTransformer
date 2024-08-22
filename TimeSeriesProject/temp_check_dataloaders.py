import torch
from fasd_data_loader import myDataLoader, FasdDataset
import numpy as np
import os
import pandas as pd

file = "C:/Users/Annah/Documents/dev/maci/TimeSeriesTransformer/FASD_data/test/snip10_test.csv"

df = pd.read_csv(file)

print(df.shape)

data = df.iloc[:, :-1].values
labels = df.iloc[:, -1:].astype(dtype=int).values

print(f"data shape: {data.shape}")
print(f"labels shape: {labels.shape}")



# data_dir = "C:/Users/Annah/Documents/dev/maci/TimeSeriesTransformer/FASD_data/train"

# train_dataset = FasdDataset(data_dir = data_dir, train=True)

# print(f"Number of files in dataset: {len(train_dataset.files)}")

# for i in range(len(train_dataset.files)):
#   data_path = os.path.join(train_dataset.data_dir, train_dataset.files[i])
#   df = pd.read_csv(data_path)
#   data = df.iloc[:, :-1].values
#   labels = df.iloc[:, -1:].astype(dtype=int).values
#   print(f"File: {train_dataset.files[i]}")
#   print(f"Data shape: {data.shape}")
#   print(f"Labels shape: {labels.shape}")

# train_loader = myDataLoader(batch_size=1).getDataLoader()['train']
# val_loader = myDataLoader(batch_size=1).getDataLoader()['val']

# # Print training data
# print("Training Data:")
# for batch in train_loader:
#     data, labels = batch
#     print("Data size:")
#     print(data.size())
#     print("Labels size:")
#     print(labels.size())
#     # Remove break to print all batches
#     # break
  

# # Print validation data
# print("Validation Data:")
# for batch in val_loader:
#     data, labels = batch
#     print("Data size:")
#     print(data.size())
#     print("Labels size:")
#     print(labels.size())
#     # Remove break to print all batches
#     # break