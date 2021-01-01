from outer import *
from h import *

from colormod import *
from helper import *

def genbutton(q,dic,op=None):
  ret='<a href="'+handlelink(q["link"])+'"'
  if (not op is None) and op["newpage"]:ret+=' target="_blank"'
  col="red"
  if "color" in q.keys():col=q["color"]
  if not col in dic.keys():dic[col]=len(list(dic.keys()))+1
  ret+=' class="l'+str(dic[col])+'"'
  cold=darken(col)
  # ret+=' style="background-color:'+col+';'#+'a:hover, a:active {background-color: '+cold+';}'
  if "fontcolor" in q.keys():
    # ret+='color:'+q["fontcolor"]+'"'
    ret+=' style="color:'+q["fontcolor"]+';"'
  else:
    # ret+='"'
    pass
  
  ret+='>'+q["label"]+'</a>'
  
  return ret


def buttoned(q):
  
  cdic={}
  
  options={}
  options["newpage"]="newpage" in q.keys() and bool(q["newpage"])
  
  
  ret1="\n<br>".join([genbutton(zw,cdic,op=options) for i,zw in enumerate(q["q"]) if i%2==0])
  ret2="\n<br>".join([genbutton(zw,cdic,op=options) for i,zw in enumerate(q["q"]) if i%2==1])
  

  ret='''<div class="row">
  <div class="column">##1##</div>
  <div class="column">##2##</div>
</div>'''.replace("##1##",ret1).replace("##2##",ret2)
 
  
  head=[h2]
  title=""
  if "t" in q:title=q["t"]
  if "title" in q:title=q["title"]
  if "hidetitle" in q:title=""
  if len(title)>0:
    ret="<h3>"+title+"</h3>\n"+ret
    
    head.append('''<style>
h3 {
color: #999999;
font-family: arial, sans-serif;
font-size: 8vw;
font-weight: bold;
margin-top: 0px;
margin-bottom: 1px;
text-align: center;

}


</style>''')
    
  

  head.append('''<style>
a:link, a:visited {
  color: white;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  width: 100%;
  height: 25vh;
  font-size: 5vw;
  vertical-align: center;
  margin-bottom=1000px;
}


</style>''')
  # x="""a:hover, a:active {
    # background-color: red;
  # }"""
  for color in cdic.keys():
    head.append('''<style>
    
a.l===:link, a.l===:visited {background-color:###;}
a.l===:hover, a.l===active {background-color:§§§;border-style: solid;border-color:§§§}
</style>
'''.replace("===",str(cdic[color])).replace("###",gohex(color)).replace("§§§",darken(color)))
  
  
  return adaptouter(q,ret,head)
  
  
  
