import os
import shutil
import multiprocessing
import timeit

os.chdir('/home/unimind/Documents/Classes/HPC/HW2/')
from multiprocessing import Process
Process(target=shutil.copytree, args=['src', 'dst']).start()
