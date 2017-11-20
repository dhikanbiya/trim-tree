<?php 
echo "hello this is nothing, just a comment";
$input = $_GET['inp'];
$inp2 = $_POST['oo'];

$sql = "SELECT * from tbl_ex where id =".$input;
$sql2 = "SELECT * from tbl_ex where id =".mysql_real_escape_string($input);

$query  = "SELECT * FROM products WHERE id LIKE '%$prod%'";
$result = mssql_query($query);

?>