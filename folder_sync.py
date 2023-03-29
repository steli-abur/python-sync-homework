import os
import shutil
import time
import logging
import datetime

path = input("Introduce File Path")
copyto = input("Introduce Destination Directory")
interval = input("Introduce Interval in seconds(must be a number)")

while True:
    files = os.listdir(path)
    files.sort()
    for f in files:
        src = path + '\\' + f
        dst = copyto + '\\' + f
        try:
            if os.stat(src).st_mtime < os.stat(dst).st_mtime:
                continue
        except OSError:
            pass
            print("Am copiat un fisier")
            shutil.copy(src, dst)
            f = open(copyto + '\\' + 'Log.txt', "a")
            f.write(str(datetime.datetime.now()) + ' | ' + 'Files copied from ' + path + ' to ' + copyto + '!' + '\n')
            f.close()
            print('Files copied from ' + path + ' to ' + copyto + '!')

    time.sleep(float(interval))
