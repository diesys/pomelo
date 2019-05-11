<?php 
echo "<!doctype html>
<html lang='it'>
  <head>
    <!-- Required meta tags -->
    <meta charset='utf-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1, shrink-to-fit=no'>
    <link rel='stylesheet' media='screen' href='https://fontlibrary.org/face/raleway' type='text/css'/>
    <link rel='icon' href='img/antipong_favicon.png'>
    
    <style>
        body { 
            font-family: 'RalewayRegular'; 
            font-weight: normal; 
            font-style: normal; 
            background: #eee;
            margin: 0;
            padding: 0;
            left: 0;
            top: 0;
        }

        #logo {
            position: fixed;
            top: 0px;
            left: 10px;
            z-index: 100;
            border-radius: 100px;
            border: 15px solid #fff;
            box-shadow: 0 9px 30px -21px rgba(0,0,0,.7);
        }
        
        #titolo {
            box-shadow: 0 -5px 30px -8px rgba(0,0,0,.4);
            position: fixed;
            width: 100%;
            top: 0;
            left: 0;
            margin: 0;
            background: #fff;
            padding: .9em;
            height: 80px;
        }
        #titolo > h1 {
            position: absolute;
            left: 48%;
            transform: translateX(-50%);
        }
        #content {
            margin-top: 145px;
        }
    </style>
    
    
    ";


$output = shell_exec('./tornelo.py --update prova aaaa bbbb 0.5 --web 2>&1');



echo "<body><center>";

echo "
<img id='logo' src='img/antipong_idle2.gif' height='100px' width='100px' alt='Smash the ball, smash fascism!' />
<span id='titolo'>
        <h1 id='itolo'>Torneo '19</h1></span>";

echo "<div id='content'><h2>CLASSIFICA</h2>", "<br/>";

$output2 = shell_exec('./tornelo.py --ranking prova --web 2>&1');
# inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output2));

// echo "<br/>== PARTITE ==", "<br/><br/>";
echo "<h2>PARTITE</h2>", "<br/>";
$output3 = shell_exec('./tornelo.py --match prova --web 2>&1');
# inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output3));

echo "</div></center></body></html>";

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
