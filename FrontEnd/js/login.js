var $parag;
var dispName;
var $welcomeDisp;
var isLoggedIn = false;

$(document).ready(function() {
    // On ready things
    // Also gets run when the login modal is closed

    // Page specific js

    if (document.title == "StockStokr - Home") {
        $parag = $("#parag");
    }
    if (document.title == "StockStokr - Account") {
        $welcomeDisp = $("#welcomeDisp");
        loadAccountPage();
    }
});

function closeModal() {
    $("#login").modal("toggle");
}

function requestLogin() {


    var uri = "http://stockstockrs.duckdns.org/ss/v1.0/login";
    var info = $('form').serializeArray();
    console.log(info);
    var email = info[0].value;
    var pswd = info[1].value;
    var dataToSend = {
        "email": email,
        "pswd": pswd
    }

    $.post({
        url: uri,
        contentType: "application/json",
        dataType: 'json',
        data: JSON.stringify(dataToSend),
        success: function(data) {
            isLoggedIn = true;
            alert(data.response[0].dispName);
            dispName = data.response[0].dispName;
            //alert(dispName);
            window.location.assign("account.html");
        },
        error: function(data) {
            alert(data.responseJSON.response);
        }
    });
}

function loadAccountPage() {
    //console.log(dispName);
    $welcomeDisp.text("Welcome " + dispName);

}
