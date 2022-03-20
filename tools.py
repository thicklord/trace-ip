import os
import shutil
from datetime import datetime


def dir_mkr(specified_path):  # function that creates a directory if it does not exist
    if not os.path.isdir(specified_path):
        os.makedirs(specified_path)


def archive_temp_files(in_files: list, remove=True):
    # function to archive temporary files used to build out results; removes archived files by default
    
    # date string
    dt_string = datetime.now().strftime("%Y-%m-%d_%H%M")
    
    # full archive path
    archive_dir = os.path.join(os.getcwd(), "%s_%s" % (dt_string, os.path.splitext(in_files[0])[0]))
    
    dir_mkr(archive_dir)
    
    for i in in_files:
        shutil.move(i, archive_dir)
    
    archive_file = shutil.make_archive(archive_dir, "zip", archive_dir)
    
    if remove:
        shutil.rmtree(archive_dir)
    
    return archive_file
