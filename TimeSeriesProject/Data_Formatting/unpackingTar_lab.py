import tarfile
import shutil
import os
import pandas as pd

control_suffix = 'control_rawdata.npy'
fasd_suffix = 'fasd_rawdata.npy'

control_path = '/lab/mksimmon/Downloads/TimeSeriesTransformer/FASD_data/control_data'
fasd_path = '/lab/mksimmon/Downloads/TimeSeriesTransformer/FASD_data/fasd_data'

num_snips = 71

def extract_and_sort(path_to_file, snip):
    with tarfile.open(path_to_file, 'r:gz') as tar:
        for member in tar.getmembers():
            if member.name.endswith(control_suffix):
                tar.extract(member, path=control_path)
            if member.name.endswith(fasd_suffix):
                 tar.extract(member, path=fasd_path)



#extract_and_sort(f'/lab/raid/datasets/eye-tracking/iLab-Queens-FASD-EyeTracking/FASD eye dataset/snip1.tar.gz', 1)
               

for snip in range(1,num_snips):
    extract_and_sort(f'/lab/raid/datasets/eye-tracking/iLab-Queens-FASD-EyeTracking/FASD eye dataset/snip{snip}.tar.gz', snip)


    prev_name_control = f'/lab/mksimmon/Downloads/TimeSeriesTransformer/FASD_data/control_data/snip{snip}/{control_suffix}'
    prev_name_fasd = f'/lab/mksimmon/Downloads/TimeSeriesTransformer/FASD_data/fasd_data/snip{snip}/{fasd_suffix}'

    new_name_control = f'/lab/mksimmon/Downloads/TimeSeriesTransformer/FASD_data/control_data/snip{snip}/snip{snip}_control_rawdata.npy'
    new_name_fasd = f'/lab/mksimmon/Downloads/TimeSeriesTransformer/FASD_data/fasd_data/snip{snip}/snip{snip}_fasd_rawdata.npy'

    os.rename(prev_name_control, new_name_control)
    os.rename(prev_name_fasd, new_name_fasd)

    bad_path_control = new_name_control
    bad_path_fasd = new_name_fasd

    if not os.path.isfile(new_name_control):
        shutil.move(bad_path_control, control_path)
    if not os.path.isfile(new_name_fasd):
        shutil.move(bad_path_fasd, fasd_path)
    
    if os.path.isfile(new_name_control):
        os.remove(new_name_control)
        os.rmdir(f'/lab/mksimmon/Downloads/TimeSeriesTransformer/FASD_data/control_data/snip{snip}')
    if os.path.isfile(new_name_fasd):
        os.remove(new_name_fasd)
        os.rmdir(f'/lab/mksimmon/Downloads/TimeSeriesTransformer/FASD_data/fasd_data/snip{snip}')
