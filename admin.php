<?php

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

?>

<!doctype html>
<html lang='it'>
    <head>
        <!-- Required meta tags -->
        <title>Admin | TornELO</title>
        <meta charset='utf-8'>
        <meta name="description" content="TornELO is a self-hosted opensource tournament server and script" />
        <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'>
        <link rel='stylesheet' media='screen' href='https://fontlibrary.org/face/raleway' type='text/css'/>
        <link rel='icon' href='img/antipong_favicon.png'>
        <meta name="HandheldFriendly" content="true" />
        <meta name="mobile-web-app-capable" content="yes">

        <!-- bootstrap -->
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
        <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
        
        <link rel="stylesheet" href="css/main.css" />
    </head>
    
    <body>
        
        <img id='logo' src='img/antipong_idle2.gif' height='90px' width='90px' alt='Smash the ball, smash fascism!' />
        
        <span id='titolo'>
            <h1 id='itolo'>Admin | TornELO</h1>
            <a href="./" class="adminButton">
                <ion-icon size="large" name="paper"></ion-icon>
            </a>
        </span>
        
        <div id='content' class="container-fluid">
            
            <h2 class="titleSection">Modifica torneo</h2>
            <h3 class="titleSection">Aggiungi partita</h3>
            
            <center>
                  <form action="./admin.php" method="post">
                    <input type="hidden" name="torneo" value="singolo">
                  <div class="input-group input-padding">
                      <div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon1">singolo</span>
                    </div>
                    <select class="custom-select" name="giocatore1" required>
                      <option value="" disabled selected>Giocatore 1</option>
                      <?php  echo shell_exec('./tornelo.py -g singolo --web 2>&1'); ?>
                    </select>

                    <select class="custom-select" name="giocatore2" required>
                      <option value="" disabled selected>Giocatore 1</option>
                      <?php  echo shell_exec('./tornelo.py -g singolo --web 2>&1'); ?>
                    </select>
                    
                    <select class="custom-select col-2" id="inputGroupSelect02" name="esito" required>
                        <option disabled selected value="">esito</option>
                        <option value="1">1</option>
                        <option value="0">2</option>
                    </select>
                    
                    <div class="input-group-append">
                        <button class="btn btn-outline-secondary bg-danger text-white bigFontButton" type="submit">
                            <ion-icon size="large" name="ios-add"></ion-icon>
                        </button>
                    </div>
                   </div>
               		</form>

              		<form action="./admin.php" method="post">
                    <input type="hidden" name="torneo" value="doppio">
                        <div class="input-group input-padding">
                    <div class="input-group-prepend">
                        <span class="input-group-text" id="basic-addon1">doppio</span>
                    </div>
                    <select class="custom-select" name="giocatore1" required>
                			<option value="" disabled selected>Giocatore 1</option>
                      <?php  echo shell_exec('./tornelo.py -g doppio --web 2>&1'); ?>
                    </select>

                    <select class="custom-select" name="giocatore2" required>
                			<option value="" disabled selected>Giocatore 2</option>
                      <?php  echo shell_exec('./tornelo.py -g doppio --web 2>&1'); ?>
                    </select>
                    
                    <select class="custom-select col-2" id="inputGroupSelect02" name="esito" required>
                        <option disabled selected value="">esito</option>
                        <option value="1">1</option>
                        <option value="0">2</option>
                    </select>
                    
                    <div class="input-group-append">
                        <button class="btn btn-outline-secondary bg-danger text-white bigFontButton" type="submit">
                            <ion-icon size="large" name="ios-add"></ion-icon>
                        </button>
                    </div>
                    </div>
		                </form>


		<?php $torneo = $_POST["torneo"]; $g1 = $_POST["giocatore1"]; $g2 = $_POST["giocatore2"]; $esito = $_POST["esito"]; if ($g1==$g2 and $g1!=""){?>
		<div class="alert alert-danger" role="alert"> Un giocatore non può giocare contro se stesso.</div>
    <?php } elseif ($torneo and $g1 and $g2 and $esito> -1){ ?>
      <div class="alert alert-primary" role="alert"> Nuova partita inserita: <?php echo $g1." contro ".$g2.", esito = ".$esito." (torneo ".$torneo.")<br><strong>";
      $command = "./tornelo.py -u $torneo \"$g1\" \"$g2\" $esito --web 2>&1"; echo $command."</strong><br>"; echo shell_exec("./tornelo.py -u $torneo \"$g1\" \"$g2\" $esito --web 2>&1"); echo "</div>";}?>

            <h3 class="titleSection">Aggiungi giocatore</h3>
            <form action="./admin.php" method="post">
                  <div class="input-group input-padding">
                    <div class="input-group-append">
                    <select class="custom-select" name="torneo" required>
                      <option value="" disabled selected>Torneo</option>
                      <option value="singolo">singolo</option>
                      <option value="doppio">doppio</option>
                    </select>
                    <input type="text" class="form-control" name="nome" required placeholder="Nome">
                        <button class="btn btn-outline-secondary bg-danger text-white bigFontButton" type="submit">
                            <ion-icon size="large" name="ios-add"></ion-icon>
                        </button>
                    </div>
         		</form>
<?php
        $torneo = $_POST["torneo"];
        $nome = $_POST["nome"];
        if ($torneo and $nome){
          $out = shell_exec("./tornelo.py -a $torneo $nome --web 2>&1");
          if ($out ==""){ ?>
            <div class="alert alert-primary" role="alert">Nuova iscrizione al torneo <?php echo $torneo.": ".$nome;?>.</div>

<?php }else{ ?>
  <div class="alert alert-danger" role="alert">Errore: il giocatore <?php echo $nome ?> è già iscritto al torneo <?php echo $torneo; ?>.</div>
<?php }}?>

            </center>

        </div>
            
        <div class="container-fluid">
            <h2 class='titleSection'>Dettagli TORNEi</h2>
            <div class="row">
                <div class="col-sm-6 col-xs-push-6">
                    <h2 class='titleSection'>Singolo</h2>
                    <div class="row">

                        <div class="col-lg-6">        
                            <h4 class='titleSection'>Ranking</h4>
                            <p class="centered">
                                <?php 
                                    $output1 = shell_exec('./tornelo.py --ranking singolo --web 2>&1');
                                    # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                                    echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output1));
                                ?>
                            </p>
                        </div>
                    
                        <div class="col-lg-6">
                            <h4 class='titleSection'>Partite</h4>
                            <p class="centered">
                                <?php 
                                $output2 = shell_exec('./tornelo.py --match singolo --web 2>&1');
                                # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                                echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output2));
                                ?>
                            </p>
                        </div>
                    </div>
                </div>
                <div class="col-sm-6 col-xs-push-6">
                    <h2 class='titleSection'>Doppio</h2>

                    <div class="row">

                        <div class="col-lg-6">
                            <h4 class='titleSection'>Ranking</h4>
                            <p class="centered">
                                <?php 
                                $output1 = shell_exec('./tornelo.py --ranking doppio --web 2>&1');
                                # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                                echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output1));
                                ?>
                            </p>
                        </div>
                        
                        <div class="col-lg-6">
                            <h4 class='titleSection'>Partite</h4>
                            <p class="centered">
                                <?php 
                                    $output2 = shell_exec('./tornelo.py --match doppio --web 2>&1');
                                    # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                                    echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output2));
                                ?>
                            </p>
                        </div>
                    </div>
                </div>
            </div>

        </div>

        <!-- ion-icons -->
        <script src="https://unpkg.com/ionicons@4.5.5/dist/ionicons.js"></script>

    </body>
</html>
