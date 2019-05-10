<?php 

$command = escapeshellcmd('./torneo.py --test');
$output = shell_exec($command);

# inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output));

?>