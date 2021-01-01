

from h import *


def adaptouter(q,inn,head=None):
  if head is None:head=[]
  t=""
  if "t" in q.keys():t=q["t"]
  if "title" in q.keys():t=q["title"]
  
  if "color" in q.keys():head.append('''<style>body{background-color:###;}</style>'''.replace("###",q["color"]))
  
  return outerlayer(inn,head,t=t)
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

</head>
<body>
{germanice(inn)}
</body>
</html>
"""