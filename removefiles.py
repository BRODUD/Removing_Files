import shutil
import os
import time

def Removefiles() :
       path = input('Enter Path: ')
       isExist = os.path.exists(path)
       days = time.time()
       var =  os.walk(path)
       root_ext= os.path.splitext(path)
       date_created = os.stat(path).st_ctime
       isFile = os.path.isfile(path)
       if (days-date_created>=2629743):
           if(isFile==True):
               os.remove(path)
           else:
               shutil.rmtree(path)

Removefiles()