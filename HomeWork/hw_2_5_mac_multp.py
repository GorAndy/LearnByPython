import subprocess
import os
import glob
from multiprocessing import Process


def mod_size(name_file):
    subprocess.run(['sips', '--resampleWidth', '200', name_file, '--out', new_path])


origin_path = './source'
new_path = 'result'
if not os.path.isdir(new_path):
    os.mkdir(new_path)
files = glob.glob(os.path.join(origin_path, '*.jpg'))


proc1 = Process(target=mod_size, args=(files[0],))
proc2 = Process(target=mod_size, args=(files[1],))
proc3 = Process(target=mod_size, args=(files[2],))
proc4 = Process(target=mod_size, args=(files[3],))
proc5 = Process(target=mod_size, args=(files[4],))

proc1.start()
proc2.start()
proc3.start()
proc4.start()
proc5.start()

proc1.join()
proc2.join()
proc3.join()
proc4.join()
proc5.join()
