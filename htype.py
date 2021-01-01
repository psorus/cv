from helper import *



def linkingpage(q):
  return """
<!DOCTYPE html>
<html>
<script>
function redirect() {
  location.replace("###")
}
</script>
<body onload="redirect()">



</body>
</html> 

  """.replace("###",handlelink(q["q"]))