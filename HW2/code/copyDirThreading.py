import os
import shutil
from threading import Thread

os.chdir('/home/unimind/Documents/Classes/HPC/HW2/')

Thread(target=shutil.copytree, args=['src', 'dst']).start()

