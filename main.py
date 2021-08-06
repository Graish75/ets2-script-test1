import os
import glob
import shutil

copiato = False
while 1:
    if os.path.exists('E:\music') == "True":
        os.system(r"xcopy E:\music\* C:\Users\%username%\Documents\Euro Truck Simulator 2\music")
    else:
        if os.path.exists('E:\music') == "False":
            os.system(r"del C:\Users\%username%\Documents\Euro Truck Simulator 2\music\*")
exit()
