<?php 
require_once ('MysqliDb.php');
$db = new MysqliDb (getenv('MYSQL_SERVER'),getenv('MYSQL_USER'),getenv('MYSQL_PASS'),getenv('MYSQL_DB'));
