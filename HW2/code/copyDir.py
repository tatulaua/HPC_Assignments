import os
import shutil

pathOfDirs = '/home/unimind/Documents/Classes/HPC/HW2'
   
print("Print Directories in superior directory before copying its subdirectory:")  
print(os.listdir(pathOfDirs))  
   
   
# Source path  
src = '/home/unimind/Documents/Classes/HPC/HW2/src'
   
# Destination path  
dest = '/home/unimind/Documents/Classes/HPC/HW2/dst'
   
# Copy the content of source to destination  
destination = shutil.copytree(src, dest)  


print("Print Directories in superior directory after copying its subdirectory:")  
print(os.listdir(pathOfDirs))  
   



    

