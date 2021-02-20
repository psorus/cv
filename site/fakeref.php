<?php
$mail=$_GET["mail"];
//if(isset($_GET("too"))){$to=$_GET("too");}
$nam=$_GET["nam"];
//if(isset($_GET("code"))){$code=$_GET("code");}
$add=$_GET["add"];
$subject = "Reference Letter ".$nam."";

$message = "
<html>
<head>
<title>Reference Letter ".$nam."</title>
</head>
<body>
<h1>This is not a real reference letter but a proof that reference letters can be send by anybody</h1>
<h3>#### does not know about this email, so please dont respond to this email</h3>
<h3>Send your own reference letters at <a href='psorus.de/fakeref.html'>psorus.de/fakeref.html</a></h3>
<br><br><br>
<p>Dear ".$add.",</p>
<p>".$nam." is a model student, a great scientist and somebody I am proud to call a friend.</p>
<p>Regards,</p>
<p>####</p>
</body>
</html>
";

// Always set content-type when sending HTML email
$headers = "MIME-Version: 1.0" . "\r\n";
$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

// More headers
$add1 = 'From: <weinberg@physics.utexas.edu>' . "\r\n";
$add2 = 'From: <merkel@bundeskanzler.de>' . "\r\n";
$add3 = 'From: <bill.gates@microsoft.com>' . "\r\n";

mail($mail,$subject,str_replace("####","Stephen Weinberg",$message),$headers.$add1);
mail($mail,$subject,str_replace("####","Angela Merkel",$message),$headers.$add2);
mail($mail,$subject,str_replace("####","Bill Gates",$message),$headers.$add3);




?>
