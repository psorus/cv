# from gohtml import *

from helper import *
from outer import *

from h import *


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

def addlist(h,x,order=False,typ="timeline"):
  x="\n".join([f"<li>{xx}</li>" for xx in x])
  ac=f"""<###l class="{typ}">
{x}
</###l>"""
  if order:
    ac=ac.replace("###","o")
  else:
    ac=ac.replace("###","u")
  return h,ac

def assuretyped(q):
  ret=[]
  for qq in q:
    if len(qq)==2:qq.append("full")
    ret.append(qq)
  return ret

def adddict(h,x):
  x=assuretyped(x)
  
  s=set([xx[-1] for xx in x if not xx[-1]=="full"])
  
  
  q=[]
  for ss in s:
    h,q=addcbox(h,q,ss,ss)
  
  q="\n".join(q)
  
  x="\n".join([f"<dt class='{y[2]}'>{y[0]}</dt><dd class='{y[2]}'>{y[1]}</dd>" for y in x])
  ret=f"""{q}
<dl>
{x}
</dl>"""
  return h,ret


def adaptive(h,x,d):
  if type(x) is list:
    order=False
    typ="none"
    if "order" in d.keys():
      typ=d["order"]
    if "typ" in d.keys():
      typ=d["typ"]
    if typ=="none":
      return adddict(h,x)
    return addlist(h,x,order=order,typ=typ)

  if type(x) is dict:
    return adddict(h,x)

def addbox(h,q,i,label=""):
  q.append(f"""<fieldset>
<legend>{label}</legend>
{i}
</fieldset>""")
  return h,q

def docollumn(h,q):
  ret=[]
  for ac in q:
    h,sub=adaptive(h,ac["q"],ac)
    h,ret=addbox(h,ret,sub,ac["label"])
  return h,ret

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


def doublelist(p):
  q=p["q"]
  h=[]
  h,c1=docollumn(h,q[0])
  h,c2=docollumn(h,q[1])
  rel=[]
  h,rel=collums(h,rel,c1,c2)
  
  h.append(h1)
  h.append(h2)
  h.append(h3)
  h.append(h4)
  h.append(h5)
  h.append(h6)
  
  # if not buttons is None:
    # acx,ach=generatebuttons(buttons)
    # h.append(ach)
    # rel.append(acx)
  
  with open("style/doublelist.css","r") as f:
    h.append(f.read())
  
  ret=adaptouter(p,rel,h)
    
  ret=replacer(ret,add=p)
  
  return ret
  return visualise(q["q"])