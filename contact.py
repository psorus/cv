from outer import *
from h import *

from colormod import *
from helper import *



def contact(q):
  ret=[]
  head=[]
  
  
  if "name" in q.keys():
    ret.append('<h1 style="name">%s</h1>' % q["name"])
  if "email" in q.keys():
    ret.append('<h3 style="email">Email:</h3>')
    for mail in q["email"]:
      ret.append('<p style="email">%s <a href="mailto:%s">Write me</a></p>' % (mail,mail))
  if "phone number" in q.keys():
    ret.append('<h3 style="phone">phone number:</h3>')
    for number in q["phone number"]:
      ret.append('<p style="phone">%s <a href="tel:%s">Call me</a></p>' % (number,number))
  if "other" in q.keys():
    ret.append('<h3 style="other">Other:</h3>')
    for ot in q["other"]:
      ret.append('<p style="other">%s</p>' % ot)

  with open("style/contact.css","r") as f:
    head.append(f.read())












  return adaptouter(q,ret,head)

# def contactpdf(q):