import os
from const import *


from gopdf import *

os.system("python export.py")
if not onlinemode:
  transform("site/","pdfs/")
  os.system("cp pdfs/s/cv.pdf finalise/amsterdam/page5.pdf")