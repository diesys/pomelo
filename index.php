<?php 

// $command = escapeshellcmd('./tornelo.py --testImp');
// $output = shell_exec($command);
// $output = shell_exec('./tornelo.py --testNew ciao 2>&1');
// $output = shell_exec('./tornelo.py --testImp CIAO 2>&1');

############## MUST USE (for the moment) --impweb param to avoid permission errors
$output = shell_exec('./tornelo.py --update prova michele giovanni 1 --web 2>&1');

echo '====== TORNEO', PHP_EOL;
$output = shell_exec('./tornelo.py -i prova --web 2>&1');

# inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output));

// echo '====== CLASSIFICA', PHP_EOL;
// $output2 = shell_exec('./tornelo.py -r prova --web 2>&1');

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
