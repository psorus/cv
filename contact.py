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
      ret.append('<p style="email">%s <a href="mailto:%s">Write this email</a></p>' % (mail,mail))
  if "phone number" in q.keys():
    ret.append('<h3 style="phone">phone number:</h3>')
    for number in q["phone number"]:
      ret.append('<p style="phone">%s <a href="tel:%s">Call this number</a></p>' % (number,number))
  if "birthday" in q.keys():
    ret.append('<h3 style="birthday">Born at:</h3>')
    for ot in q["birthday"]:
      ret.append('<p style="birthday">%s</p>' % ot)
  if "website" in q.keys():
    ret.append('<h3 style="website">See also:</h3>')
    for ot in q["website"]:
      ret.append('<p style="website"><a href="%s" target="_blank">%s</a></p>' % (ot,ot))
  if "other" in q.keys():
    ret.append('<h3 style="other">Other:</h3>')
    for ot in q["other"]:
      ret.append('<p style="other">%s</p>' % ot)
  if "notes" in q.keys():
    ret.append('<h3 style="notes">Notes:</h3>')
    for ot in q["notes"]:
      ret.append('<p style="notes">%s</p>' % ot)
  if "back" in q.keys():
    for ot in q["back"]:
      ret.append('<p style="back">%s</p>' % ot)
  
      

  with open("style/contact.css","r") as f:
    head.append(f.read())












  return adaptouter(q,ret,head)

# def contactpdf(q):