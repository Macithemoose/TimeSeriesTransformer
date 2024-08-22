import numpy as np
import pandas as pd
import torch 
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import OneHotEncoder
import os
 
from sklearn.model_selection import train_test_split
 
class FasdDataset(Dataset):
    def __init__(self, data_dir, train=True):
        super().__init__()
        self.data_dir = data_dir
        self.files = os.listdir(data_dir)
        self.train = train
        
        # Prepare data splits per file
        self.file_data_splits = []
        for file in self.files:
            data_path = os.path.join(self.data_dir, file)
            df = pd.read_csv(data_path)
            data = df.iloc[:, :-1].values
            labels = df.iloc[:, -1:].astype(dtype=int).values

            # Perform train/validation split for each file
            x_train, x_val, y_train, y_val = train_test_split(data, labels, test_size=0.15)

            # Store splits
            if self.train:
                self.file_data_splits.append((torch.tensor(x_train, dtype=torch.float32), torch.tensor(y_train, dtype=torch.int64)))
            else:
                self.file_data_splits.append((torch.tensor(x_val, dtype=torch.float32), torch.tensor(y_val, dtype=torch.int64)))

    def __len__(self):
        return len(self.file_data_splits)
    
    def __getitem__(self, index):
        return self.file_data_splits[index]
        

class MyTestDataLoader():
    def __init__(self, batch_size) -> None:
        self.batch_size = batch_size
        file_dir = "C:/Users/Annah/Documents/dev/maci/TimeSeriesTransformer/FASD_data/test"
 
        test_set = FasdDataset(file_dir) 
        self.dataLoader = DataLoader(test_set, batch_size=self.batch_size, shuffle=True) 

    def getDataLoader(self): 
        return self.dataLoader

class myDataLoader():
    def __init__(self, batch_size) -> None:
        self.batch_size = batch_size
        train_dir = "C:/Users/Annah/Documents/dev/maci/TimeSeriesTransformer/FASD_data/train"

        train_set = FasdDataset(train_dir, train=True)
        val_set = FasdDataset(train_dir, train=False)

        dataloaders = {
            'train': DataLoader(train_set, batch_size=batch_size, shuffle=True),
            'val': DataLoader(val_set, batch_size=batch_size, shuffle=True)
        }
        self.dataloaders = dataloaders
        

    def getDataLoader(self): 
        return self.dataloaders
