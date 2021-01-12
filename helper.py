from const import *
import os



def genampel(i,add=None):
  if add is None:add={}
  zw='<span class="###"></span>'
  ret=[]
  if i==2:
    ret.append(zw.replace("###","dotgreen"))
  else:
    ret.append(zw.replace("###","dotgray"))
  if i==1:
    ret.append(zw.replace("###","dotyellow"))
  else:
    ret.append(zw.replace("###","dotgray"))
  if i==0:
    ret.append(zw.replace("###","dotred"))
  else:
    ret.append(zw.replace("###","dotgray"))
  if "customampel" in add.keys():
    shorttex=add["customampel"][i]
  else:
    shorttex="great"
    if i==1:shorttex="good"
    if i==0:shorttex="average"
    
  return '<span class="ampel" title="'+shorttex+'">'+('\n'.join(ret))+"</span>"
def replacer(q,fontsize="1.3em",add=None):
  if add is None:add={}
  if "fs" in add.keys():fontsize=add["fs"]
  if "fontsize" in add.keys():fontsize=add["fontsize"]
  q=q.replace("{ampel:0}",genampel(0,add=add))
  q=q.replace("{ampel:red}",genampel(0,add=add))
  q=q.replace("{ampel:r}",genampel(0,add=add))
  q=q.replace("{ampel:1}",genampel(1,add=add))
  q=q.replace("{ampel:yellow}",genampel(1,add=add))
  q=q.replace("{ampel:y}",genampel(1,add=add))
  q=q.replace("{ampel:2}",genampel(2,add=add))
  q=q.replace("{ampel:green}",genampel(2,add=add))
  q=q.replace("{ampel:g}",genampel(2,add=add))
  q=q.replace("{url}",url)
  q=q.replace("##fs##",fontsize)
  q=q.replace("[n]","<br>")
  
  backcolor="red"
  if "color" in add.keys():
    backcolor=add["color"]
  q=q.replace("[backcolor]",str(backcolor))
  
  return q



def handlelink(q):
  add=""
  if addhtml:add=".html"
  # print("handling",q)
  if len(q)>1 and q[0]==":":q= "s:"+q[1:]
  if len(q)>2 and (q[:2]=="s:" or q[:2]=="s/"):return url+"/s/"+q[2:]+add
  if len(q)>0 and q[0]=="/":
    if "." in q:
      return (url+q).replace("//","/")
    else:
      return (url+q+add).replace("//","/")
  if "." in q:
    return q
  else:
    return handlelink("s:"+q)

def texmodify(x,add=None):
  x=replacer(x,add=add)
  fs={q.replace(".sml",""):"s/"+q.replace(".sml","") for q in os.listdir("s/") if os.path.isfile("s/"+q)}



  for key in fs.keys():
    x=x.replace(f"[LI {key}:",f'<a href="{handlelink(fs[key])}">')
  x=x.replace("NK]","</a>")
  return x
  
if __name__=="__main__":
  q="s:abstract_master"
  print(q)
  print(handlelink(q))
