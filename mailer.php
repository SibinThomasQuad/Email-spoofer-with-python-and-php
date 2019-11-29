<?php
$to = $_GET['toemail'];
$subject = $_GET['subject'];
$message = $_GET['message'];
$fromemail = $_GET['fromemail'];
$fromname = $_GET['fromname'];
$lt= '<';
$gt= '>';
$sp= ' ';
$from= 'From:';
$headers = $from.$fromname.$sp.$lt.$fromemail.$gt;
mail($to,$subject,$message,$headers);
?>
