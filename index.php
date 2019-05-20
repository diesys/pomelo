<!doctype html>
<html lang='it'>
  <head>
    <!-- Required meta tags -->
    <title>TornELO</title>
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

<?php 
    // $output1 = shell_exec('./tornelo.py --update prova dddd cccc 0 --web 2>&1');
    # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
    // echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output1));
?>

    <body>
        <!-- <center> -->

            <img id='logo' src='img/antipong_idle2.gif' height='90px' width='90px' alt='Smash the ball, smash fascism!' />
            
            <span id='titolo'>
                <h1 id='itolo'>PingPong '19</h1>
                <a href="admin.php" class="adminButton">
                    <ion-icon size="large" name="create"></ion-icon>
                </a>
            </span>
            

            <div id="content" class="container-fluid">
                <center>
                    <img id='qr' src='img/torneloQR.gif' height='140px' width='140px' alt='http://flowin.space/tornelo/' />
                     <!-- <button class="dropdown-item btn btn-primary" data-toggle="collapse" data-target="#singoloRanking" type="button" aria-expanded="false">
                        <ion-icon name="analytics"></ion-icon> singol rank
                    </button>
                    <button class="dropdown-item btn btn-primary" data-toggle="collapse" data-target="#singoloPartite" type="button" aria-expanded="false">
                        <ion-icon name="calendar"></ion-icon> s match
                    </button>
                    <button class="dropdown-item btn btn-primary" data-toggle="collapse" data-target=".collapse-ranking" type="button" aria-expanded="true">
                        <ion-icon name="analytics"></ion-icon> ranks
                    </button>
                    <button class="dropdown-item btn btn-primary" data-toggle="collapse" data-target=".collapse-partite" type="button" aria-expanded="false">
                        <ion-icon name="calendar"></ion-icon> match
                    </button> -->
                    <!-- <div class="dropdown">
                        <button class="btn  dropdown-toggle" type="button" id="mostraMenu" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                           <ion-icon name="eye"></ion-icon> Mostra 
                        </button>
                        <div class="dropdown-menu" id="mostraMenu">
                            <button class="dropdown-item" data-toggle="collapse" data-target=".collapse-singolo" type="button" aria-expanded="true">
                                <ion-icon name="ios-contact"></ion-icon> Singolo
                            </button>
                            <button class="dropdown-item" data-toggle="collapse" data-target=".collapse-doppio" type="button" aria-expanded="false">
                                <ion-icon name="ios-contacts"></ion-icon> Doppio
                            </button>
                        </div>
                    </div> -->
                    <br>
                    <div class="btn-group mr-2" role="group" aria-label="First group">
                        <button class="btn btn-outline-primary" onclick="$(this).toggleClass('active')" data-toggle="collapse" data-target=".collapse-singolo" type="button" aria-expanded="true">
                            <ion-icon name="ios-contact" size="large"></ion-icon> <ion-icon name="ios-contact" size="large"></ion-icon> 
                        </button>
                        <button class="btn btn-outline-danger" onclick="$(this).toggleClass('active')" data-toggle="collapse" data-target=".collapse-doppio" type="button" aria-expanded="false">
                            <ion-icon name="ios-contacts" size="large"></ion-icon> <ion-icon name="ios-contacts" size="large"></ion-icon>
                        </button>
                    </div>
                </center> 
                
                <div class="row">
                    <!-- <div class="col-sm-6 col-xs-push-6"> -->
                    <!-- <div class="col-sm-12 col-xs-push-12"> -->
                        <!-- <h2 class="titleSection">Singolo</h2> -->
                        
                        <!-- <div class="row collapse-singolo" id="singolo"> -->

                            <div class="col collapse collapse-ranking collapse-singolo" id="singoloRanking">        
                                <h4 class='titleSection'>Ranking (singolo)</h4>
                                <p class="centered">
                                    <?php 
                                        $output1 = shell_exec('./tornelo.py --ranking singolo --web 2>&1');
                                        echo $output1;
                                        # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                                        // echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output1));
                                    ?>
                                </p>
                            </div>
                        
                            <div class="col collapse collapse-partite collapse-singolo" id="singoloPartite">
                                <h4 class='titleSection'">Partite (singolo)</h4>
                                <p class="centered">
                                    <?php 
                                    $output2 = shell_exec('./tornelo.py --match singolo --web 2>&1');
                                    echo $output2;
                                    # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                                    // echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output2));
                                    ?>
                                </p>
                            </div>
                        <!-- </div> -->
                    <!-- </div> -->
                    <!-- <div class="col-sm-6 col-xs-push-6"> -->
                    <!-- <div class="col-sm-12 col-xs-push-12"> -->
                        <!-- <h2 class="titleSection">Doppio</h2> -->

                        <!-- <div class="row collapse-doppio" id="doppio"> -->

                            <div class="col collapse collapse-ranking collapse-doppio" id="doppioRanking">
                                <h4 class='titleSection'>Ranking (doppio)</h4>
                                <p class="centered">
                                    <?php 
                                    $output1 = shell_exec('./tornelo.py --ranking doppio --web 2>&1');
                                    echo $output1;
                                    # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                                    // echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output1));
                                    ?>
                                </p>
                            </div>
                            
                            <div class="col collapse collapse-partite collapse-doppio" id="doppioPartite">
                                <h4 class='titleSection'>Partite (doppio)</h4>
                                <p class="centered">
                                    <?php 
                                        $output2 = shell_exec('./tornelo.py --match doppio --web 2>&1');
                                        echo $output2;
                                        # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                                        // echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output2));
                                        ?>
                                </p>
                            </div>
                        <!-- </div> -->
                    <!-- </div> -->
                </div>

            </div>

        <!-- </center> -->
        <!-- ion-icons -->
        <script src="https://unpkg.com/ionicons@4.5.5/dist/ionicons.js"></script>

    </body>
</html>

<?php
    // echo $output2

# get a json and dump
// $json = file_get_contents('data/ping/ping.json');  
// $json_output = json_decode($json, true); 
// echo $json_output;

// foreach ($json_output as $trend){         
//    echo $trend['text']."\n";     
//   } 


# trasforma il dizionario python in un array php
// $data =  json_decode($output, true);
// print_r($data);
    // if (count($data->stand)) {
    //     // Open the table
    //     echo "<table>";

    //     // Cycle through the array
    //     foreach ($data->stand as $idx => $stand) {

    //         // Output a row
    //         echo "<tr>";
    //         echo "<td>$stand->afko</td>";
    //         echo "<td>$stand->positie</td>";
    //         echo "</tr>";
    //     }

    //     // Close the table
    //     echo "</table>";
    // }

    // function build_table($array){
    //     // start table
    //     $html = '<table>';
    //     // header row
    //     $html .= '<tr>';
    //     foreach($array[0] as $key=>$value){
    //             $html .= '<th>' . htmlspecialchars($key) . '</th>';
    //         }
    //     $html .= '</tr>';

    //     // data rows
    //     foreach( $array as $key=>$value){
    //         $html .= '<tr>';
    //         foreach($value as $key2=>$value2){
    //             $html .= '<td>' . htmlspecialchars($value2) . '</td>';
    //         }
    //         $html .= '</tr>';
    //     }

    //     // finish table and return it

    //     $html .= '</table>';
    //     return $html;
    // }

    // echo build_table($data);
?>