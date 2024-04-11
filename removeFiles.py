import os
import shutil
path="C:/Users/adininja/projects"
time.gmtime(0)
ctime = os.stat(path).st_ctime
return ctime
