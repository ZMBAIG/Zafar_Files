__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os 
import shutil
from glob import glob

def clean_cache():
    dir_path = os.getcwd()
    folder = f'{dir_path}/files/cache'
    if os.path.isdir(folder):
        shutil.rmtree(folder)
    return os.mkdir(folder)

def cache_zip(zip_file, cache_dir):
    shutil.unpack_archive(zip_file, cache_dir)

def cached_files():
    return glob('/files/cache/*')

def find_password(cached_files_list):
    for file in cached_files_list:
        with open(file) as check_file:
            lines = check_file.readlines()
        for line in lines:
            if 'password' in line:
                return line

clean_cache()
print(find_password(cached_files()))
