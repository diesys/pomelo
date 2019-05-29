<?php //header("Location: ."); ?>

<?php
    function alert($msg) {
        echo "<script type='text/javascript'>alert('$msg');</script>";
    }

    $valid_passwords = array ("uova" => "frittata");
    $valid_users = array_keys($valid_passwords);

    $user = $_SERVER['PHP_AUTH_USER'];
    $pass = $_SERVER['PHP_AUTH_PW'];

    $validated = (in_array($user, $valid_users)) && ($pass == $valid_passwords[$user]);

    if (!$validated) {
        header('WWW-Authenticate: Basic realm="My Realm"');
        header('HTTP/1.0 401 Unauthorized');
        die ("Not authorized");
    }

    if(isset($_POST["giocatore1"]) and isset($_POST["giocatore2"]) and isset($_POST["torneo"]) and isset($_POST["esito"])) {
        $torneo = $_POST["torneo"]; $g1 = $_POST["giocatore1"]; $g2 = $_POST["giocatore2"]; $esito = $_POST["esito"];
    
        if (!($g1==$g2 and $g1!="")) {
            if ($torneo and $g1 and $g2 and $esito> -1) {
                // echo "<strong>".$g1."</strong>  vs  <strong>".$g2."</strong> (".$esito.")<br/><ion-icon name='md-checkmark-circle-outline'></ion-icon> inserito nel torneo ".$torneo."!";
                    echo shell_exec("./tornelo.py -u $torneo \"$g1\" \"$g2\" $esito  2>&1"); 
                    echo shell_exec("./tornelo.py --gen-index 2>&1"); 
                    alert("Partita aggiunta al $torneo: \"$g1\" vs \"$g2\" ($esito)");
                    echo "</div>";
                }
            }
            echo("./tornelo.py -u $torneo \"$g1\" \"$g2\" $esito --web 2>&1"); 
            shell_exec('whoami');
            print(shell_exec('whoami'));

    }

    foreach ($_POST as $key => $value) {
        echo '<p>'.$key.": ".$value.'</p>';
    } 

?>