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

                echo "<div id='content'><h2>CLASSIFICA</h2>", "<br/>";

                $output2 = shell_exec('./tornelo.py --ranking prova --web 2>&1');
                # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output2));

                // echo "<br/>== PARTITE ==", "<br/><br/>";
                echo "<h2>PARTITE</h2>", "<br/>";
                $output3 = shell_exec('./tornelo.py --match prova --web 2>&1');
                # inserisce una <br/> dopo il newline (nl2br) e sostituisce i tre spazi (formattati in python json)
                echo nl2br(str_replace("   ", '&nbsp;&nbsp;&nbsp;&nbsp;', $output3));
            
            
                echo "</div>";
            ?>



            <!-- <img id='qr' src='img/torneloQR.gif' height='140px' width='140px' alt='http://flowin.space/tornelo/' /> -->

        </center>
    </body>
</html>