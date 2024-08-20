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

    def __len__(self):
        return len(self.files)
    
    def __getitem__(self, index): 
        data_path = os.path.join(self.data_dir, self.files[index])
        data = pd.read_csv(data_path).iloc[:,:-1].values
        labels = pd.read_csv(data_path).iloc[:,-1:].astype(dtype=int).values

        x_train, x_val, y_train, y_val = train_test_split(data, labels, test_size=0.15)

        x_train = torch.tensor(x_train)
        y_train = torch.tensor(y_train)
        x_val = torch.tensor(x_val)
        y_val = torch.tensor(y_val)
    
        return x_train, y_train if self.train else x_val, y_val
        

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
