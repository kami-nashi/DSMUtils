<?php

$sql_server = '10.68.25.61';
$sql_user = 'dsm_user';
$sql_password = 'password';
$sql_database = 'dsmutils_csv';

if (!$link = mysql_connect($sql_server, $sql_user, $sql_password)) {
    echo 'Could not connect to mysql';
    exit;
}

if (!mysql_select_db($sql_database, $link)) {
    echo 'Could not select database';
    exit;
}

?>
