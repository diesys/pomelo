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
    $output1 = shell_exec('./tornelo.py --update prova dddd cccc 0 --web 2>&1');
    # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
    // echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output1));
?>

    <body>
        <!-- <center> -->

            <img id='logo' src='img/antipong_idle2.gif' height='70px' width='70px' alt='Smash the ball, smash fascism!' />
            
            <span id='titolo'>
                <h1 id='itolo'>Torneo '19</h1>
            </span>

            <div id="content" class="container-fluid">
                <center>
                    <img id='qr' src='img/torneloQR.gif' height='140px' width='140px' alt='http://flowin.space/tornelo/' />
                </center> 
                
                <h2 class='titleSection'>Dettagli TORNEi</h2>

                <div class="row">
                    <div class="col-sm-6 col-xs-push-6">
                        <h2 class='titleSection'>Singolo</h2>
                        <div class="row">

                            <div class="col-md-6">        
                                <h4 class='titleSection'>Ranking</h4>
                                <p class="centered">
                                    <?php 
                                        $output1 = shell_exec('./tornelo.py --ranking prova --web 2>&1');
                                        # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                                        echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output1));
                                    ?>
                                </p>
                            </div>
                        
                            <div class="col-md-6">
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
                    </div>
                    <div class="col-sm-6 col-xs-push-6">
                        <h2 class='titleSection'>Doppio</h2>

                        <div class="row">

                            <div class="col-md-6">
                                <h4 class='titleSection'>Ranking</h4>
                                <p class="centered">
                                    <?php 
                                    $output1 = shell_exec('./tornelo.py --ranking cippo --web 2>&1');
                                    # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                                    echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output1));
                                    ?>
                                </p>
                            </div>
                            
                            <div class="col-md-6">
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

            </div>

        <!-- </center> -->
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