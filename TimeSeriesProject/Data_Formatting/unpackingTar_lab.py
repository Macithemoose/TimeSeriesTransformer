import tarfile
import shutil
import os
import pandas as pd

control_suffix = 'control_rawdata.npy'
fasd_suffix = 'fasd_rawdata.npy'

control_path = '/lab/mksimmon/Downloads/TimeSeriesProject/fasd_data/control_data'
fasd_path = '/lab/mksimmon/Downloads/TimeSeriesProject/fasd_data/fasd_data'

num_snips = 71

def extract_and_sort(path_to_file, snip):
    with tarfile.open(path_to_file, 'r:gz') as tar:
        for member in tar.getmembers():
            if member.name.endswith(control_suffix):
                tar.extract(member, path=control_path)
            if member.name.endswith(fasd_suffix):
                 tar.extract(member, path=fasd_path)
                 df = pd.DataFrame(list(f'{fasd_path}/snip{snip}/{fasd_suffix}'))
                 df.to_csv(f'{fasd_path}/snip{snip}/snip{snip}_fasd.csv')
               

for snip in range(1, num_snips):
    extract_and_sort(f'/lab/raid/datasets/eye-tracking/iLab-Queens-FASD-EyeTracking/FASD eye dataset/snip{snip}.tar.gz', snip)
    os.remove(f'{fasd_path}/snip{snip}/snip{snip}_fasd.csv')
    os.remove(f'{control_path}/snip{snip}/snip{snip}_control.csv')
