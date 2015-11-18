<?php
	$name = $_POST['name'];
	$phone = $_POST['phone'];
	$email = $_POST['email'];
	$message = $_POST['message'];
	$how = $_POST['how'];
	 	
	$to = 'sarahtstander@gmail.com';
	$mainsubject = 'Comment Form';
	 	
	$body = "This is a message from your Canterbury Dental website, canturburydental.com.\n From: $name\n Phone: $phone\n E-mail: $email\n Contact By: $how\n Message: $message";
 
	if ($_POST['submit']) {
		if (mail ($to,$mainsubject,$body,$from))
		{
			echo "<p>Message sent.</p>";
		}
		else
		{
			echo "<p>Please try again.</p>";
		}
	}
?>