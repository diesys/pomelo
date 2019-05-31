<?php header("Location: .?acon=".$_POST['action']."&torneo=".$_POST["torneo"]."&g1=".$_POST["giocatore1"]."&g2=".$_POST["giocatore2"]."&gS=".$_POST["giocatoreS"]."&gD=".$_POST["giocatoreD"]."&nG=".$_POST["nuovoGiocatore"]."&r=".$_POST["esito"]);  ?>
<!-- <?php header("Location: .?action=".$_POST['action']); ?> -->

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

    if(isset($_POST['action'])) {
        $action = $_POST['action'];

        if($action == 'update') {
            if(isset($_POST["giocatore1"]) and isset($_POST["giocatore2"]) and isset($_POST["torneo"]) and isset($_POST["esito"])) {
                $torneo = $_POST["torneo"]; $g1 = $_POST["giocatore1"]; $g2 = $_POST["giocatore2"]; $esito = $_POST["esito"];

                if (!($g1==$g2 and $g1!="")) {
                    if ($torneo and $g1 and $g2 and $esito> -1) {
                        $command = "./tornelo.py -u $torneo \"$g1\" \"$g2\" $esito  2>&1";
                        $alert_msg = "Partita aggiunta al $torneo: \"$g1\" vs \"$g2\" ($esito)";
                    }
                }
            }
        } 

        elseif($action == 'delete') {
            if(isset($_POST["giocatoreS"])){
                $torneo = 'singolo'; $giocatore = $_POST["giocatoreS"];
            }
            elseif(isset($_POST["giocatoreD"])) {
                $torneo = 'doppio'; $giocatore = $_POST["giocatoreD"];
            }
            else {
                $command = '';
                $alert_msg = 'Qualche errore rimuovendo il giocatore!';
            }
            $command = "./tornelo.py -d $torneo \"$giocatore\" 2>&1";
            $alert_msg = "$giocatore. rimosso dal torneo \"$torneo\"";
        } 
        
        elseif($action == 'add') {
            if(isset($_POST["nuovoGiocatore"]) and isset($_POST["torneo"])) {
                $torneo = $_POST["torneo"]; $giocatore = $_POST["nuovoGiocatore"];
                $command = "./tornelo.py -a $torneo \"$giocatore\" 2>&1";
                $alert_msg = "$giocatore. ora fa parte del torneo \"$torneo\"";
            }
            else {
                $command = '';
                $alert_msg = 'Qualche errore aggiungendo il giocatore!';
            }
        }

        else {
            $command = '';
            $alert_msg = 'Nessuna azione selezionata!';
        }
        
        
        print(shell_exec('whoami'));
        echo ($command.'\n\n'.$alert_msg);
        echo shell_exec($command);
        // costruisce il nuovo index
        echo shell_exec("./tornelo.py --gen-index 2>&1"); 
        alert($alert_msg);
    }


    foreach ($_POST as $key => $value) {
        echo '<p>'.$key.": ".$value.'</p>';
    } 

?>