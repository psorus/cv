import os
import json
from codecs import open
from colormod import *

from buttoned import *
from contact import *
from doublelist import *
from readstr import *
from htype import *

posfun={"darken":darken,"sdarken":sdarken}


def smartml(q):

  fn=f"s/{q}.sml"

  if not os.path.isfile(fn):
    return "Not a valid path"
  with open(fn,"r", 'utf-8') as f:
    ac=f.read()
  
  istext=False
  # try:
  if 1:
    ac=eval(ac,posfun)#yes security risk, but...way less errors than json.loads()
    
  # except:
    # istext=True
  if istext or (type(ac) is not dict) or (not "type" in ac) or ac["type"]=="text":istext=True
  # print("THIS IS ",istext,type(ac),istext , (type(ac) is not dict) , (not "type" in ac))# , ac["type"]=="text")
  if istext:
    return readstr(ac)
  t=ac["type"]
  if t=="buttons":return buttonedpdf(ac)
  if t=="contact":return contactpdf(ac)
  if t=="doublelist":return doublelistpdf(ac)
  if t=="link":return linkingpagepdf(ac)
  
  return "cannot understand this file"