import numpy as np
import pandas as pd
import torch 
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import OneHotEncoder
import os
 
from sklearn.model_selection import train_test_split
 
class FasdDataset(Dataset):
    def __init__(self, data_dir):
        super().__init__()
        self.data_dir = data_dir
        self.files = os.listdir(data_dir)

    def __len__(self):
        return len(self.files)
    
    def __getitem__(self, index): 
        return self.data, self.labels

class MyTestDataLoader():
    def __init__(self, batch_size) -> None:
        self.batch_size = batch_size 
        file_out_test = pd.read_csv('snip10_test.csv')
        
        x_test = file_out_test.iloc[:,:-1].values
        y_test = file_out_test.iloc[:,-1:].astype(dtype=int).values
        #y_test = y_test.ravel()
        #y_test = y_test.long()  
 
        test_set = FasdDataset(x = x_test, y = y_test) 
        self.dataLoader = DataLoader(test_set, batch_size=self.batch_size, shuffle=True,  ) 

    def getDataLoader(self): 
        return self.dataLoader

class myDataLoader():
    def __init__(self, batch_size) -> None:
        self.batch_size = batch_size
        file_out_train = pd.read_csv('snip10_train.csv') 

        x_train = file_out_train.iloc[:,:-1].values
        y_train = file_out_train.iloc[:,-1:].astype(dtype=int).values 
        #y_train = y_train.ravel()
        #y_train = y_train.long()
        x_train, x_val, y_train, y_val = train_test_split(x_train,y_train,test_size=0.15)  

        train_set = FasdDataset(x = x_train, y = y_train) 

        val_set = FasdDataset(x = x_val, y = y_val) 

        dataloaders = {
            'train': DataLoader(train_set, batch_size=batch_size, shuffle=True),
            'val': DataLoader(val_set, batch_size=batch_size, shuffle=True)
        }
        self.dataloaders = dataloaders
        

    def getDataLoader(self): 
        return self.dataloaders
