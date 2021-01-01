from colour import Color as color

def darken(s):
  c=color(s)
  c2=color(rgb=[max(float(q)*0.9-0.05,0) for q in c.get_rgb()])
  return c2.get_hex()
def sdarken(s):
  c=color(s)
  c2=color(rgb=[max(float(q)*0.95-0.025,0) for q in c.get_rgb()])
  return c2.get_hex()

def gohex(s):
  return color(s).get_hex()
