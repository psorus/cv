import pdfkit as p
import os

options={"page-size":"A4"}

def trafoone(fro,too):
  try:
    print("transforming",fro)
    p.from_file(fro,too.replace(".html","")+".pdf",options=options)
  except:
    pass

def transform(fro,too):
  if not os.path.isdir(too):os.makedirs(too)
  for pat in [fro+q for q in os.listdir(fro)]:
    if os.path.isfile(pat) and not ".pdf" in pat:
      trafoone(pat,pat.replace(fro,too))
    if os.path.isdir(pat):
      pat=pat+"/"
      transform(pat,pat.replace(fro,too))


if __name__=="__main__":
  # print(os.listdir("site/"))
  # exit()
  transform("site/","pdfs/")

