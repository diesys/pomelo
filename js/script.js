function toggleTheme() {
    // UI
    $('body').toggleClass('dark');

    // tabelle
    $('table').toggleClass('table-dark');
    $('tr.success').toggleClass('bg-success');
    $('tr.success').toggleClass('table-success');    
}

function getUrlVars() {
    var vars = {};
    var parts = window.location.href.replace(/[?&]+([^=&]+)=([^&]*)/gi, function (m, key, value) {
        vars[key] = value;
    });
    return vars;
}

/////////// Auto NIGHT MODE ///////////////////
window.onload = function () {

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