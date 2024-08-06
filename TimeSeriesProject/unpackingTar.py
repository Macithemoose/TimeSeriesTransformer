import tarfile
import shutil
import os

control_suffix = 'control_rawdata.npy'
fasd_suffix = 'fasd_rawdata.npy'

control_path = r'C:/Users/Annah/Documents/dev/maci/FASD_data/control_data'
fasd_path = r'C:/Users/Annah/Documents/dev/maci/FASD_data/fasd_data'

num_snips = 71

def extract_all_files(tar_file_path, control_suffix, fasd_suffix, control_path, fasd_path):
  with tarfile.open(tar_file_path,'r:gz') as tar:
    for member in tar.getmembers():
      #print(member.name)
      if member.name.endswith(control_suffix):
        #print(member.name)
        tar.extract(member, path = control_path)
      elif member.name.endswith(fasd_suffix):
        #print(member.name)
        tar.extract(member, path = fasd_path)

for snip in range(2, num_snips):
  prev_name_control = f'C:/Users/Annah/Documents/dev/maci/FASD_data/control_data/snip{snip}/{control_suffix}'
  prev_name_fasd = f'C:/Users/Annah/Documents/dev/maci/FASD_data/fasd_data/snip{snip}/{fasd_suffix}'

  new_name_control = f'C:/Users/Annah/Documents/dev/maci/FASD_data/control_data/snip{snip}/snip{snip}_control_rawdata.npy'
  new_name_fasd = f'C:/Users/Annah/Documents/dev/maci/FASD_data/fasd_data/snip{snip}/snip{snip}_fasd_rawdata.npy'

  os.rename(prev_name_control, new_name_control)
  os.rename(prev_name_fasd, new_name_fasd)

  tar_file_path = f'C:/Users/Annah/Documents/dev/maci/snips/snip{snip}.tar.gz'
  bad_path_control = new_name_control
  bad_path_fasd = new_name_fasd
  extract_all_files(tar_file_path,control_suffix, fasd_suffix, control_path, fasd_path)
  
  if not os.path.isfile(new_name_control):
    shutil.move(bad_path_control, control_path)
  if not os.path.isfile(new_name_fasd):
    shutil.move(bad_path_fasd, fasd_path)


