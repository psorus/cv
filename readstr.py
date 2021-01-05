from outer import *





def readstr(q):
  if type(q) is str:q={"q":q,"color":"whitesmoke"}
  
  with open("style/text.css","r") as f:
    h=f.read()
  
  ac=q["q"]
  ac=ac.replace("\n","[n]")
  
  
  return adaptouter(q,'<div>'+ac+'</div>',[h])