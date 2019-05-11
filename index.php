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
    <link rel="stylesheet" href="css/main.css" />
    <meta name="HandheldFriendly" content="true" />
	<meta name="mobile-web-app-capable" content="yes">    

    <body>
        <center>

            <img id='logo' src='img/antipong_idle2.gif' height='70px' width='70px' alt='Smash the ball, smash fascism!' />
            
            <span id='titolo'>
                <h1 id='itolo'>Torneo '19</h1>
            </span>

            <?php 
                $output = shell_exec('./tornelo.py --update prova aaaa dddd 0 --web 2>&1');

                echo "<h2 class='titleSection'>CLASSIFICA</h2>", "<br/>";

                $output2 = shell_exec('./tornelo.py --ranking prova --web 2>&1');
                # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output2));

                // echo "<br/>== PARTITE ==", "<br/><br/>";
                echo "<h2 class='titleSection'>PARTITE</h2>", "<br/>";
                $output3 = shell_exec('./tornelo.py --match prova --web 2>&1');
                # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output3));
            
            
                echo "</div>";
            ?>



            <img id='qr' src='img/torneloQR.gif' height='140px' width='140px' alt='http://flowin.space/tornelo/' />

        </center>
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