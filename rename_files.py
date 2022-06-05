import os
from pathlib import Path

cwd = os.getcwd()
extension = '.jpg'
labels = {}

for root, dirs, files in os.walk(cwd):
    for file in files:
        if file.endswith(extension):
            file_path = os.path.join(root, file)
            path_parts = Path(root).parts
            label = path_parts[-1]      
            
            if label in labels:
                labels[label] += 1
            else:
                labels[label] = 1

            #file_name = os.path.splitext(file)[0]
            file_new = label + str(labels[label]) + extension
            os.rename(file_path, os.path.join(root, file_new))
            print(file_new)