// function CopyToClipboard() { // www.aspforums.net%2fThreads%2f517506%2fCopy-browser-url-to-clipboard-on-button-click-using-JavaScript-and-jQuery%2f
//     var text = document.createElement("textarea");
//     text.innerHTML = window.location.href;
//     Copied = text.createTextRange();
//     Copied.execCommand("Copy");
// }

function toggleTheme() {
    // UI
    $('body').toggleClass('dark');

    // tabelle
    $('table').toggleClass('table-dark');
    $('tr.success').toggleClass('bg-success');
    $('tr.success').toggleClass('table-success');
    
    // browser color
    if($('body').hasClass('dark'))
        color = '#17191c';
    else
        color = '#ffffff';
    
    $('#browserColor').attr('content', color);
    $('#browserColorwp').attr('content', color);
    $('#browserColorap').attr('content', color);

    console.log('changing theme...');
}

function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function (m, key, value) {
        vars[key] = value;
    });
    return vars;
}

// function enableOpts(opt) {

// }

// function rmSoloMatch(sel_index_value) {
//     const sel2 = $('#selGioc2')[0].options;
//     // $('#selGioc2')[0].options = $('#selG ioc1')[0].options
//     console.log($('#selGioc2')[0].lenght, sel_index_value)

//     for (i = 1; i < sel2.lenght; i++) {
//         // sel2.options.item(i).disabled = true;
//     //     // console.log(sel2.options[i])
//         console.log(i);
//     }
//     // console.log("Enabling all options...", i)

//     // sel2.options[sel_index_value].disabled = true
//     // $('#selGioc2')[0].options[sel_index_value].disabled = !$('#selGioc2')[0].options[sel_index_value].disabled
//     // console.log("Removing selected player from the other list...")
// }

window.onload = function () {
    // clipboard.js
    new ClipboardJS('.btn');

    /////////// Auto NIGHT MODE ///////////////////
    var urlVars = getUrlVars();
    var d = new Date();
    var hour = d.getHours();

    if (hour < 7 | hour > 18) {
        toggleTheme();
        console.log('auto-enabling dark mode...')
    } else 
        if (urlVars["night"]) {
            toggleTheme();
            console.log('URL var detected: enabling dark mode...')
        } 
    
    /////////// BINDING ///////////////////////////

    // easteregg theme #code from: https://stackoverflow.com/a/7845282
    var DELAY = 400,
        clicks = 0,
        timer = null;

    $(function () {
        $("#logo").bind("click", function (e) {
                clicks++; //count clicks

                if (clicks === 1) {
                    timer = setTimeout(function () {
                        console.log('Logo clicked, going home...')
                        window.location.replace('/pomelo');
                        clicks = 0; //after action performed, reset counter
                    }, DELAY);
                } else {
                    clearTimeout(timer); //prevent single-click action
                    toggleTheme();
                    console.log('Logo dbl-clicked, changing theme...')
                    clicks = 0; //after action performed, reset counter
                }
            })
            .bind("dblclick", function (e) {
                e.preventDefault(); //cancel system double-click event
            });
    });
    
    // open menu
    $('#admin_button').bind('click', function(){
        $('#menu').slideToggle();
        $('#admin_icon').toggleClass('active')
        console.log('Menu button clicked, toggling menu...')
    });

    // close menu (when active) on outside click
    $('#content').bind('click', function() {
        if ($('#menu').css('display') != 'none') {
            $('#menu').slideUp();
            $('#admin_icon').toggleClass('active');
        }
    });
 
    // click on qr copy on clipboard
    $('#qr').bind('click', function() {
        CopyToClipboard();
    });


    // select torneo
    
    $('#buttonRanking').bind('click', function() {
        $(this).toggleClass('active');
        $('#ranking').slideToggle();
        // $('#ranking').fadeToggle();
        // $('#ranking').toggleClass('');
        console.log('Toggle ranking table...');
    });
    
    $('#buttonMatches').bind('click', function() {
        $(this).toggleClass('active');
        $('#partite').slideToggle();
        // $('#partite').fadeToggle();
        console.log('Toggle matches table...');
    });
    
    $('#buttonShare').bind('click', function() {
        $('#shareMenu').slideToggle()
    });

}