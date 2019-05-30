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


    // select tornei
    $('#buttonSingolo').bind('click', function() {
        if ($('#singoloRanking').is(':visible') | $('#singoloPartite').is(':visible')) {
            $(this).removeClass('active');
            $('.buttonSingolo').removeClass('active');
            $('.collapse-singolo').fadeOut();
        } else {
            $(this).addClass('active');
            $('.buttonSingolo').addClass('active');
            $('.collapse-singolo').fadeIn();
        } 
    });
    
    $('#buttonRankSingolo').bind('click', function() {
        bS = $('#buttonSingolo').hasClass('active');
        bPS = $('#buttonPartSingolo').hasClass('active');
        bRS = $('#buttonRankSingolo').hasClass('active');
        
        if ( bS && bPS && bRS ) {
            $('#singoloRanking').fadeOut();
            $(this).removeClass('active');
        } else if ( bS && bPS ) {
            $('#singoloRanking').fadeIn();
            $(this).addClass('active');
        } else if ( bS ) {
            $('#singoloRanking').fadeOut();
            $(this).removeClass('active');
            $('#buttonSingolo').removeClass('active');
        } else {
            $('#singoloRanking').fadeIn();
            $(this).addClass('active');
            $('#buttonSingolo').addClass('active');
        }        
    });
    
    $('#buttonPartSingolo').bind('click', function() {
        bS = $('#buttonSingolo').hasClass('active');
        bPS = $('#buttonPartSingolo').hasClass('active');
        bRS = $('#buttonRankSingolo').hasClass('active');

        if (bS && bPS && bRS) {
            $('#singoloPartite').fadeOut();
            $(this).removeClass('active');
        } else if (bS && bRS) {
            $('#singoloPartite').fadeIn();
            $(this).addClass('active');
        } else if (bS) {
            $('#singoloPartite').fadeOut();
            $(this).removeClass('active');
            $('#buttonSingolo').removeClass('active');
        } else {
            $('#singoloPartite').fadeIn();
            $(this).addClass('active');
            $('#buttonSingolo').addClass('active');
        }   
    });

    $('#buttonDoppio').bind('click', function() {
        if ($('#doppioRanking').is(':visible') | $('#doppioPartite').is(':visible')) {
            $(this).removeClass('active');
            $('.buttonDoppio').removeClass('active');
            $('.collapse-doppio').fadeOut();
        } else {
            $(this).addClass('active');
            $('.buttonDoppio').addClass('active');
            $('.collapse-doppio').fadeIn();
        } 
    });

    $('#buttonRankDoppio').bind('click', function () {
        bS = $('#buttonDoppio').hasClass('active');
        bPS = $('#buttonPartDoppio').hasClass('active');
        bRS = $('#buttonRankDoppio').hasClass('active');

        if (bS && bPS && bRS) {
            $('#doppioRanking').fadeOut();
            $(this).removeClass('active');
        } else if (bS && bPS) {
            $('#doppioRanking').fadeIn();
            $(this).addClass('active');
        } else if (bS) {
            $('#doppioRanking').fadeOut();
            $(this).removeClass('active');
            $('#buttonDoppio').removeClass('active');
        } else {
            $('#doppioRanking').fadeIn();
            $(this).addClass('active');
            $('#buttonDoppio').addClass('active');
        }
    });

    $('#buttonPartDoppio').bind('click', function () {
        bS = $('#buttonDoppio').hasClass('active');
        bPS = $('#buttonPartDoppio').hasClass('active');
        bRS = $('#buttonRankDoppio').hasClass('active');

        if (bS && bPS && bRS) {
            $('#doppioPartite').fadeOut();
            $(this).removeClass('active');
        } else if (bS && bRS) {
            $('#doppioPartite').fadeIn();
            $(this).addClass('active');
        } else if (bS) {
            $('#doppioPartite').fadeOut();
            $(this).removeClass('active');
            $('#buttonDoppio').removeClass('active');
        } else {
            $('#doppioPartite').fadeIn();
            $(this).addClass('active');
            $('#buttonDoppio').addClass('active');
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