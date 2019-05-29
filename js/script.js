function toggleTheme() {
    // UI
    $('body').toggleClass('dark');

    // tabelle
    $('table').toggleClass('table-dark');
    $('tr.success').toggleClass('bg-success');
    $('tr.success').toggleClass('table-success');

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
    
    /////////// Auto NIGHT MODE ///////////////////
    var urlVars = getUrlVars();
    var d = new Date();
    var hour = d.getHours();

    if (urlVars["night"]) {
        if (urlVars["night"] == "true") {
            nightMode();
        } else if (urlVars["night"] == "false") {
            dayMode();
        }
        
    } else {
        if ((hour > 0 || hour < 7) && (hour > 0 || hour < 7)) {
            toggleTheme();
            console.log('auto-enabling dark mode...')
        } 
    }
}