import os
import shutil
from tqdm import tqdm

def collect_files(directory):
    all_files = []
    for path, subdirs, files in tqdm(os.walk(directory)):
        for name in files:
            filename = os.path.join(path, name)
            all_files.append(filename)
    return all_files

def copy_files(target_dir, files):
    for file in tqdm(files):
        name = file.split('/')[-1]
        new_path = os.path.join(target_dir, name)
        shutil.copy(src=file, dst=new_path)

dataset_dir = '/home/john/datasets/VCTK-Corpus/wav48/'
target_dir = '/home/john/datasets/VCTK-Corpus/allwav/'
files = collect_files(directory=dataset_dir)
copy_files(target_dir=target_dir, files=files)
