import os
from smartml import *
from helper import *

from io import open

from const import *
if addhtml:
  add=".html"
else:
  add=""

exportpath="site/"
if os.path.isdir(exportpath):
  import shutil
  shutil.rmtree(exportpath, ignore_errors=True)
os.makedirs(exportpath)

if not os.path.isdir(exportpath+"s/"):
  os.makedirs(exportpath+"s/")
  
def handlefile(q,base="s/",endi=".sml"):
  # with open(base+q+endi,"r") as f:
  return texmodify(smartml(q))

def trafofile(q,p):
  with open(exportpath+p+add,"w", encoding="utf-8") as f:
    f.write(handlefile(q))

trafofile("index","index")
os.system("cp permasite/* site -r")


for fil in [q[:q.find(".")] for q in os.listdir("s")]:
  print("doing",fil)
  trafofile(fil,"s/"+fil)









  










