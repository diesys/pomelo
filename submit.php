<?php 
    $host = gethostname(); 
    $domain = explode("/", $host)[1];
    if(isset($_GET['torneo'])){
        $torneo_dir = str_replace(' ', '_', $_GET['torneo']);
        $url = $domain."/pomelo"."/r/".$torneo_dir; 
    } else { // index
        $url = $domain."/pomelo"; 
    }
    $vars = "?action=".$_POST['action'];
    
    header("Location: ".$url.$vars);

    
    $safeParse = "/[0-9a-zA-Z ]/";

    if(isset($_POST['action']) and preg_match("/^[a-z]/", $_POST['action'])) {
    // if(isset($_POST['action'])) {
        // $action = escapeshellarg($_POST['action']);
        $action = $_POST['action'];
        
        // torneo gets parsed inside options, torneo as escaped var, _input as raw input (only using in url)
        if(isset($_GET['torneo']))
            $torneo_input = $_GET['torneo'];
        elseif(isset($_POST['torneo']))
            $torneo_input = $_POST['torneo'];
        else
            $torneo_input = FALSE;
        // if($torneo_input )
        // if(preg_match("/[^0-9a-zA-Z ]/", $torneo_input))
            $torneo = escapeshellarg($torneo_input);
        // else {
            // $torneo = 'ERROR, invalid name';
            // $_GET['torneo'] = "ERROR";
        // }

        if($action == 'update') {
            if(isset($_POST["giocatore1"]) and isset($_POST["giocatore2"]) and isset($_POST["esito"])) {
                $g1 = escapeshellarg($_POST["giocatore1"]); $g2 = escapeshellarg($_POST["giocatore2"]); escapeshellarg($esito = $_POST["esito"]);

                if (!($g1==$g2 and $g1!="")) {
                    if ($torneo and $g1 and $g2 and $esito > -1) {
                        $command = "./pomelo.py $torneo -u $g1 $g2 $esito  2>&1";
                        $alert_msg = "Partita aggiunta al $torneo: \"$g1\" vs \"$g2\" ($esito)";
                    }
                }
            }
        } 

        elseif($action == 'goto') {
            $command = '';
            // echo preg_match_all($safeParse, $torneo);                
            if(preg_match($safeParse, $torneo)) {
                header('Location: ./r/'.$torneo_input);
            }
        }
        
        elseif($action == 'create') {
            // check ALPHANUMERIC (with space)
            // if (ctype_alnum($torneo) and $torneo != "") {
            if (preg_match($safeParse, $torneo) and $torneo != "") {
                $command = "./pomelo.py $torneo -n 2>&1";
                $alert_msg = "Creato un nuovo torneo: $torneo";
                $torneo_dir = str_replace(' ', '_', $torneo_input);
                header('Location: ./r/'.$torneo_dir);
            } else {
                $command = '';
                $alert_msg = "Errore creando il nuovo torneo $torneo";
            }
        }
            
        elseif($action == 'delete') {
            if(isset($_POST["giocatore"])) {
                // $torneo = $_GET["torneo"]; // passed from the py tournament template
                $giocatore = escapeshellarg($_POST["giocatore"]);
                
                $command = "./pomelo.py $torneo -d $giocatore 2>&1";
                $alert_msg = "$giocatore. rimosso dal torneo \"$torneo\"";
            }
            else {
                $command = '';
                $alert_msg = 'Qualche errore rimuovendo il giocatore!';
            }
        } 
        
        elseif($action == 'add') {
            if(isset($_POST["nuovoGiocatore"]) and isset($_GET["torneo"])) {
                // $torneo = $_GET["torneo"]; // passed from the py tournament template
                $giocatore = escapeshellarg($_POST["nuovoGiocatore"]);
                
                // check ALPHANUMERIC (with space)
                // if (ctype_alnum($giocatore) and $giocatore != "") {
                if (preg_match($safeParse, $giocatore) and $giocatore != "") {
                    $command = "./pomelo.py $torneo -a $giocatore 2>&1";
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

        // $command_escaped = escapeshellarg($command);
        echo shell_exec($command);
        
        // costruisce il nuovo index
        // echo shell_exec("./pomelo.py \"".$torneo."\" --gen-index 2>&1");
        echo shell_exec("./pomelo.py \"".$torneo."\" --gen-index 2>&1");
        
        // alert($alert_msg);
    }
    
    
    // debug
    
    echo ("DEBUG cmd\n $command");
    echo ("DEBUG alrt\n $alert_msg");
    
    echo '<br/>POST<br/>';
    foreach ($_POST as $key => $value) {
        echo '<p>'.$key.": ".$value.'</p>';
    } 
    echo '<br/>GET<br/>';
    foreach ($_GET as $key => $value) {
        echo '<p>'.$key.": ".$value.'</p>';
    } 

?>
