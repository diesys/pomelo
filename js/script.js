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

window.onload = function () {

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
    // theme / logo
    $('#logo').bind('click', function(){
        toggleTheme();
        console.log('Logo clicked, changing theme...')
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


    // select torneo
    
    $('#buttonRanking').bind('click', function() {
        $(this).toggleClass('active');
        $('#ranking').fadeToggle();
        console.log('Toggle ranking table...');
    });
    
    $('#buttonMatches').bind('click', function() {
        $(this).toggleClass('active');
        $('#partite').fadeToggle();
        console.log('Toggle matches table...');
    });
}