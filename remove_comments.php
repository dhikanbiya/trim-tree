<?php 
$str = $argv[1];
$folder = $argv[2];
$index = $argv[3];
$string = file_get_contents($str);
$pattern = "~(?:#|//)[^\r\n]*|/\*[\s\S]*?\*/~";
$replacement = "";

$sv = preg_replace($pattern, $replacement, $string);
$save = fopen($folder.'/'.$index.'__nocomment_'.basename($str), 'aw+');
fwrite($save, $sv);
fclose($save);