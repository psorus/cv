<?php
$to=$_GET["too"];
//if(isset($_GET("too"))){$to=$_GET("too");}
$code=$_GET["code"];
//if(isset($_GET("code"))){$code=$_GET("code");}
$subject = "Activate your Account with code (".$code.")";

$message = "
<html>
<head>
<title>Activate your Acount!</title>
</head>
<body>
<p>To be able to use your Account, enter the following code</p>
<h3>".$code."</h3>
</body>
</html>
";

// Always set content-type when sending HTML email
$headers = "MIME-Version: 1.0" . "\r\n";
$headers .= "Content-type:text/html;charset=UTF-8" . "\r\n";

// More headers
$headers .= 'From: <noreply@psorus.com>' . "\r\n";

mail($to,$subject,$message,$headers);
?>
