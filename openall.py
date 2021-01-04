import os


files=["s/"+q for q in os.listdir("s")]
for fil in files:
  os.system("notepad++ "+fil)
