<?php 
require('vendor/autoload.php');
$mailbox = '{'.getenv('MAIL_SERVER').'/imap/ssl/novalidate-cert}INBOX';
$username = $_GET['email'];
$password = $_GET['password'];
$mailbox = new PhpImap\Mailbox($mailbox,$username,$password,__DIR__,'UTF-8');
try {
	$mailsIds = $mailbox->searchMailbox('SUBJECT "Zepetto"');
} catch(PhpImap\Exceptions\ConnectionException $ex) {
	// echo "IMAP connection failed: " . $ex;
	die();
}
if(!empty($mailsIds)){
	$mail = $mailbox->getMail($mailsIds[count($mailsIds)-1]);
	preg_match_all('/<strong style=\"color: #000;\">(.*)<\/strong>/', $mail->__get('textHtml'), $otp);
	echo json_encode(array('token'=>$otp[1][0]));
}
	// echo json_encode(array('token'=>'aaaaaaaaaa'));

