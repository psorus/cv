from outer import *





def readstr(q):
  if type(q) is str:q={"q":q,"color":"whitesmoke"}
  
  return adaptouter(q,q["q"],[])