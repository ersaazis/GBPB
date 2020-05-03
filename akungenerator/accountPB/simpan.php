<?php
require_once ('kon.php');
$db->where ('id', $_GET['id']);
if ($db->update ('akun', array('berhasil'=>1)))
    echo "<h1>BERHASIL</h1>";
else
    echo 'update failed: ' . $db->getLastError();
