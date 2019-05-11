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
        <!-- <center> -->

            <img id='logo' src='img/antipong_idle2.gif' height='70px' width='70px' alt='Smash the ball, smash fascism!' />
            
            <span id='titolo'>
                <h1 id='itolo'>Admin | TornELO</h1>
            </span>

            <div id='content' class="container-fluid">

                <h2 class="titleSection">Modifica torneo</h2>

                <div class="input-group input-padding">
                    <select class="custom-select col-2" id="inputGroupSelect01">
                        <option selected>Torneo</option>
                        <option value="singolo">singolo</option>
                        <option value="doppio">doppio</option>
                    </select>

                    <input type="text" aria-label="Giocatore1" placeholder="Giocatore 1" class="form-control">
                    <input type="text" aria-label="Giocatore2" placeholder="Giocatore 2" class="form-control">
                    
                    <select class="custom-select col-2" id="inputGroupSelect01">
                        <option selected>esito</option>
                        <option value="1">1</option>
                        <option value="0.5">x</option>
                        <option value="0">2</option>
                    </select>
                    
                    <div class="input-group-append">
                        <button class="btn btn-outline-secondary bg-danger text-white bigFontButton" type="button"><span class="bigFontButton">+</span></button>
                    </div>

                </div>
            </div>
            
            <div class="container">
                <!-- <h2 class='titleSection'>DUMP TORNEO</h2> -->

                <div class="row">
                        <div class="col">
                            <h2 class='titleSection'>Singolo</h2>
                                <div class="col">        
                                    <h4 class='titleSection'>Ranking</h4>
                                    <p class="centered">
                                        <?php 
                                            $output1 = shell_exec('./tornelo.py --ranking prova --web 2>&1');
                                            # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                                            echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output1));
                                        ?>
                                    </p>
                                </div>
                                <div class="col">
                                    <h4 class='titleSection'>Partite</h4>
                                    <p class="centered">
                                        <?php 
                                            $output2 = shell_exec('./tornelo.py --match prova --web 2>&1');
                                            # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                                            echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output2));
                                        ?>
                                    </p>
                                </div>
                        </div>
                            <div class="col">
                                <h2 class='titleSection'>Doppio</h2>
                                <div class="col">
                                    <h4 class='titleSection'>Ranking</h4>
                                    <p class="centered">
                                        <?php 
                                            $output1 = shell_exec('./tornelo.py --ranking cippo --web 2>&1');
                                            # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                                            echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output1));
                                        ?>
                                    </p>
                                </div>
                                <div class="col">
                                    <h4 class='titleSection'>Partite</h4>
                                    <p class="centered">
                                        <?php 
                                            $output2 = shell_exec('./tornelo.py --match cippo --web 2>&1');
                                            # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                                            echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output2));
                                        ?>
                                    </p>
                                </div>
                            </div>
                        </div>

            </div>



            <!-- <img id='qr' src='img/torneloQR.gif' height='140px' width='140px' alt='http://flowin.space/tornelo/' /> -->

        <!-- </center> -->
    </body>
</html>