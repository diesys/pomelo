<?php 

$command = escapeshellcmd('./tornelo.py --testNew ba');
$output = shell_exec($command);

# inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
// echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output));

echo $output, $command;

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
