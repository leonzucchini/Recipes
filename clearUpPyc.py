import os
import sys
import re

def clear_up_pyc(folderpath):
    """Remove all pyc files from a folder."""
    

    pyc_paths = []

    # Save paths to all .pyc files in folder to list
    for folder, subs, files in os.walk(folderpath):
        for filename in files:
            full_path = os.path.join(folder, filename)
            is_pyc = re.search(r'\.pyc', full_path)
            if is_pyc:
                pyc_paths.append(full_path)
    
    # Remove all files in list
    for path in pyc_paths:
        file = os.remove(path)