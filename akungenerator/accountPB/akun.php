<?php
include "cpaneluapi.class.php";
$uapi = new cpanelAPI(getenv('CP_USER'), getenv('CP_PASS'), getenv('CP_SERVER'));
while(1){
    $username=generateRandomName(8);
    $cek=json_decode(file_get_contents('https://www.pointblank.id/member/IdCheck?id='.$username),1)['resultCode'];
    if($cek == '0')
        break;
}
$password=generateRandomString(8);
$domain='zenbunime.com';
$email=$username."@".$domain;

$uapi->uapi->Email->add_pop(array(
    'email'           => $username,
    'password'        => $password,
    'quota'           => '1',
    'domain'          => $domain,
    'skip_update_db'  => '1',
));
$result=json_decode($uapi->json,1);
if($result['status'] == 1){

    require_once ('kon.php');
    $data = array (
        "username" => $username,
        "email" => $email,
        "password" => $password
    );
    $id = $db->insert ('akun', $data);

    // echo "<input type='text' value='$username' id='username'> <br>";
    // echo "<input type='text' value='$password' id='password'> <br>";
    // echo "<input type='text' value='$email' id='email'> <br>";
    // echo "<a id='otp' target='_blank' href='email.php?password=$password&email=$email'><h1>OTP</h1></a> <br>";
    // echo "<a id='simpan' href='simpan.php?id=$id'><h1>SIMPAN</h1></a> <br>";
    $id=1;
    echo json_encode(array(
        "id"=>$id,
        "username"=>$username,
        "password"=>$password,
        "email"=>$email,
    ));
}
function generateRandomString($length = 10) {
    $characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
    $charactersLength = strlen($characters);
    $randomString = '';
    for ($i = 0; $i < $length; $i++) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
    }
    return $randomString;
}
function generateRandomName($length = 8) {
    $characters = 'bcdfghjklmnpqrstvwxyz';
    $vocal = 'aioeo';
    $charactersLength = strlen($characters);
    $vocalLength = strlen($vocal);
    $randomString = '';
    for ($i = 0; $i < $length; $i+=2) {
        $randomString .= $characters[rand(0, $charactersLength - 1)];
        $randomString .= $vocal[rand(0, $vocalLength - 1)];
    }
    return $randomString;
}
