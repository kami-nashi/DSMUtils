<?php

header('Access-Control-Allow-Origin: *');
header('Content-Type: application/json');

function db_stuff($sql){
  require 'db_connect.php';
  $result = mysql_query($sql, $link);
  if (!$result) {
    echo "DB Error, could not query the database\n";
    echo 'MySQL Error: ' . mysql_error();
    exit;
  }

  return $result;
  }

$sql = 'select timestamp, rpm, airflow, fronto2, timing, inttemp, cooltemp, knockret, speed, throtpos from dummy_data';

$result = db_stuff($sql);

$rows = array();
  while ($r = mysql_fetch_assoc($result)) {
    $rows[] = $r;
  }

$jason = json_encode($rows);
print_r($jason);

//$nosaj = json_decode($jason);
//print_r($nosaj);

?>
