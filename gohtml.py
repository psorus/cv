import numpy as np
import json


from h import *

import os
from const import *

def germanice(q):
  q=q.replace("Ä","&Auml;")
  q=q.replace("ä","&auml;")
  q=q.replace("Ö","&Ouml;")
  q=q.replace("ö","&ouml;")
  q=q.replace("Ü","&Uuml;")
  q=q.replace("ü","&uuml;")
  q=q.replace("ß","&szlig;")

  return q


def outerlayer(inn,head="",t=""):
  if type(inn) is list:
    inn="\n".join([str(q) for q in inn])
  if type(head) is list:
    head="\n".join([str(q) for q in head])
  

  
  return f"""<!DOCTYPE html>
<html>
<head>
<title>{t}</title>
{head}
{h1}
{h2}
{h3}
{h4}
{h5}
{h6}
</head>
<body>
{germanice(inn)}
</body>
</html>
"""


def collums(h,q,i1,i2):#head list, q list, first one, second one
  if type(i1) is list:i1="\n".join([str(q) for q in i1])
  if type(i2) is list:i2="\n".join([str(q) for q in i2])
  q.append(f"""<div class="row">
  <div class="column" style="background-color:#fff;">
    {i1}
  </div>
  <div class="column" style="background-color:#fff;">
    {i2}
  </div>
</div>""")
  return h,q

def addbox(h,q,i,label=""):
  q.append(f"""<fieldset>
<legend>{label}</legend>
{i}
</fieldset>""")
  return h,q

def addlist(x,order=False,typ="timeline"):
  x="\n".join([f"<li>{xx}</li>" for xx in x])
  ac=f"""<###l class="{typ}">
{x}
</###l>"""
  if order:
    ac=ac.replace("###","o")
  else:
    ac=ac.replace("###","u")
  return ac

def addcbox(h,q,which,tex):
  ach='''<script type="text/javascript">
  function ftest1(q) {
    x=document.querySelectorAll("dd.{which}")
    for(var i=0;i<x.length;i++){
      if (x[i].style.display ==="none"){x[i].style.display="block";}else{x[i].style.display="none";}
    }
    x=document.querySelectorAll("dt.{which}")
    for(var i=0;i<x.length;i++){
      if (x[i].style.display ==="none"){x[i].style.display="block";}else{x[i].style.display="none";}
    }

  }
</script>'''
  ach=ach.replace("{which}",str(which))
  ach=ach.replace("{tex}",str(tex))
  acx=f'''  <input type="checkbox" id="hide{which}" name="hide{which}" value="True" onclick="ftest1(this)" checked>
<label for="hide{which}">show {tex}</label>'''
  
  h.append(ach)
  q.append(acx)
  return h,q

def assuretyped(q):
  ret=[]
  for qq in q:
    if len(qq)==2:qq.append("full")
    ret.append(qq)
  return ret

def adddict(x):
  x=assuretyped(x)
  
  s=set([xx[-1] for xx in x if not xx[-1]=="full"])
  
  global h
  
  q=[]
  for ss in s:
    h,q=addcbox(h,q,ss,ss)
  
  q="\n".join(q)
  
  x="\n".join([f"<dt class='{y[2]}'>{y[0]}</dt><dd class='{y[2]}'>{y[1]}</dd>" for y in x])
  ret=f"""{q}
<dl>
{x}
</dl>"""
  return ret

def addtline():
  return """<div class="timeline">
  <div class="container left">
    <div class="content">
      <h2>2017</h2>
      <p>Lorem ipsum..</p>
    </div>
  </div>
  <div class="container right">
    <div class="content">
      <h2>2016</h2>
      <p>Lorem ipsum..</p>
    </div>
  </div>
</div>"""

def genampel(i):
  zw='<span class="###"></span>'
  ret=[]
  if i==0:
    ret.append(zw.replace("###","dotred"))
  else:
    ret.append(zw.replace("###","dotgray"))
  if i==1:
    ret.append(zw.replace("###","dotyellow"))
  else:
    ret.append(zw.replace("###","dotgray"))
  if i==2:
    ret.append(zw.replace("###","dotgreen"))
  else:
    ret.append(zw.replace("###","dotgray"))
  return "\n".join(ret)

def adaptive(x,d):
  if type(x) is list:
    order=False
    typ="none"
    if "order" in d.keys():
      typ=d["order"]
    if "typ" in d.keys():
      typ=d["typ"]
    if typ=="timeline":
      return addtline()
    if typ=="none":
      return adddict(x)
    return addlist(x,order=order,typ=typ)
  if type(x) is dict:return adddict(x)

def docollumn(h,q):
  ret=[]
  for ac in q:
    
    h,ret=addbox(h,ret,adaptive(ac["q"],ac),ac["label"])
  return h,ret


def replacer(q,fontsize="1.3em"):
  q=q.replace("{ampel:0}",genampel(0))
  q=q.replace("{ampel:red}",genampel(0))
  q=q.replace("{ampel:r}",genampel(0))
  q=q.replace("{ampel:1}",genampel(1))
  q=q.replace("{ampel:yellow}",genampel(1))
  q=q.replace("{ampel:y}",genampel(1))
  q=q.replace("{ampel:2}",genampel(2))
  q=q.replace("{ampel:green}",genampel(2))
  q=q.replace("{ampel:g}",genampel(2))
  q=q.replace("##fs##",fontsize)
  return q

def visualise(q,t="",fontsize="1.3em",buttons=None):
  h=[]
  h,c1=docollumn(h,q[0])
  h,c2=docollumn(h,q[1])
  rel=[]
  h,rel=collums(h,rel,c1,c2)
  
  if not buttons is None:
    acx,ach=generatebuttons(buttons)
    h.append(ach)
    rel.append(acx)
  
  ret=outerlayer(rel,head=h,t=t)
  
  ret=replacer(ret,fontsize=fontsize)
  
  return ret
  
def visualisem1(q,t="",fontsize="1.3em"):
  global h
  h=[]
  rel=docollumn(q)
  
  
  ret=outerlayer(rel,head=h,t=t)
  
  ret=replacer(ret,fontsize=fontsize)
  
  return ret

def visualisem2(q,t="",fontsize="1.3em",buttons=None):
  global h
  h=[]
  ret=[]
  h,ret=addbox(h,ret,adaptive(q["q"],q),q["label"])
  
  ret=outerlayer(ret,head=h,t=t)
  
  ret=replacer(ret,fontsize=fontsize)
  
  return ret





#formerly texhtml
def texmodify(x):
  fs={q.replace(".txt",""):"tex/"+q.replace(".txt","") for q in os.listdir("tex/") if os.path.isfile("tex/"+q)}
  for key in fs.keys():
    x=x.replace(f"[ENTER LINK {key}]",f'<a href="{url}{fs[key]}">here</a>')
  return x
  
  

def texgenerate(q,title=""):
  front=f"<html><head><title>{title}</title></head><body>\n<h3><a href='{url}'>Back</a></h3>\n<p>"
  back="\n</p>\n</body></html>"
  return front+texmodify(q)+back


def texload(q):

  fn=f"tex/{q}.txt"

  if not os.path.isfile(fn):
    return "not found"
  with open(fn,"r") as f:
    ac=f.read()
  if not len(ac)==0:
    # print(ac[0])
    # exit()
    if ac[0]=="{" or ac[0]=="[":
      return adapt(json.loads(ac))
      return json.dumps(json.loads(ac),indent=2)
      return visualise(json.loads(ac),q)

    return germanice(texgenerate(ac))

#formerly adapt.py
def adapt(q):
  t=type(q)
  if t is str:return germanice(texgenerate(q))
  if t is dict:return visualisem2(q)
  if t is list:
    if type(q[0]) is list:
      return visualise(q)
    else:
      return visualisem1(q)