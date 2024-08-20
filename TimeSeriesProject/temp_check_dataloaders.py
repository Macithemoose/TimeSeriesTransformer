import torch
from fasd_data_loader import myDataLoader
import numpy as np

dataloaders = myDataLoader(batch_size=1).getDataLoader()

print(dataloaders['train'].dataset)