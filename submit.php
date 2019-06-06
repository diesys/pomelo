<?php 
    $host = gethostname(); 
    $domain = explode("/", $host)[1];
    if(isset($_GET['torneo'])){
        $url = $domain."/pomelo"."/r/".$_GET["torneo"]; 
    } else { // index
        $url = $domain."/pomelo"; 
    }
    $vars = "?action=".$_POST['action'];
    
    header("Location: ".$url.$vars);



    if(isset($_POST['action'])) {
        $action = $_POST['action'];

        if($action == 'update') {
            if(isset($_POST["giocatore1"]) and isset($_POST["giocatore2"]) and isset($_GET["torneo"]) and isset($_POST["esito"])) {
                $torneo = $_GET["torneo"]; $g1 = $_POST["giocatore1"]; $g2 = $_POST["giocatore2"]; $esito = $_POST["esito"];

                if (!($g1==$g2 and $g1!="")) {
                    if ($torneo and $g1 and $g2 and $esito> -1) {
                        $command = "./pomelo.py $torneo -u \"$g1\" \"$g2\" $esito  2>&1";
                        $alert_msg = "Partita aggiunta al $torneo: \"$g1\" vs \"$g2\" ($esito)";
                    }
                }
            }
        } 

        elseif($action == 'goto') {
            if(isset($_POST["torneo"])) {
                $torneo = $_POST["torneo"];
                $command = '';
                header('Location: ./r/'.$_POST["torneo"]);
            }
        }

        elseif($action == 'create') {
            if(isset($_POST["torneo"])) {
                $torneo = $_POST["torneo"];
                
                // check ALPHANUMERIC
                if (ctype_alnum($torneo) and $torneo != "") {
                    $command = "./pomelo.py \"".$_POST["torneo"]."\" -n 2>&1";
                    
                    // creates and downloads the qr-code from ext api
                    $apiQR = 'https://api.qrserver.com/v1/create-qr-code/?size=100x100&data=';
                    // $url'http://flowin.space/pomelo/r/prova' 
                    // echo shell_exec("wget -O img/QR.gif ".$apiQR.$url." 2>&1");
                    // updates the main index
                    // echo shell_exec("./pomelo.py \"".$torneo."\" --gen-index 2>&1");
                    // updates the tournament index
                    // echo shell_exec("./pomelo.py \"".$torneo."\" --gen-index 2>&1");
                    $alert_msg = "Creato un nuovo torneo: ".$_POST["torneo"];
                    }
                }
            }
            
        elseif($action == 'delete') {
            if(isset($_POST["giocatore"])) {
                $torneo = $_GET["torneo"]; // passed from the py tournament template
                $giocatore = $_POST["giocatore"];
            }
            else {
                $command = '';
                $alert_msg = 'Qualche errore rimuovendo il giocatore!';
            }
            $command = "./pomelo.py $torneo -d \"$giocatore\" 2>&1";
            $alert_msg = "$giocatore. rimosso dal torneo \"$torneo\"";
            echo $command;
        } 
        
        elseif($action == 'add') {
            if(isset($_POST["nuovoGiocatore"]) and isset($_GET["torneo"])) {
                $torneo = $_GET["torneo"]; // passed from the py tournament template
                $giocatore = $_POST["nuovoGiocatore"];
                
                // check ALPHANUMERIC
                if (ctype_alnum($giocatore) and $giocatore != "") {
                    $command = "./pomelo.py \"$torneo\" -a \"$giocatore\" 2>&1";
                    $alert_msg = "$giocatore. ora fa parte del torneo \"$torneo\"";
                }
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

        
        // print(shell_exec('whoami'));
        echo ($command."\n".$alert_msg);
        echo shell_exec($command);
        
        // costruisce il nuovo index
        echo shell_exec("./pomelo.py \"".$torneo."\" --gen-index 2>&1");
        
        // alert($alert_msg);
    }

    
    // debug
    echo '<br/>POST<br/>';
    foreach ($_POST as $key => $value) {
        echo '<p>'.$key.": ".$value.'</p>';
    } 
    echo '<br/>GET<br/>';
    foreach ($_GET as $key => $value) {
        echo '<p>'.$key.": ".$value.'</p>';
    } 

?>
