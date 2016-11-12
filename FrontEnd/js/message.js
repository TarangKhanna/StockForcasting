var $parag;
var dispSub;
var $welcomeDisp;
var isLoggedIn = false;

$(document).ready(function() {
    // On ready things
    // Also gets run when the login modal is closed

    // Page specific js

    //if (document.title == "StockStokr - Home") {
    //    $parag = $("#parag");
    //}
    //if (document.title == "StockStokr - Account") {
    //    $welcomeDisp = $("#welcomeDisp");
    //    loadAccountPage();
    //}
});

function sendMessage() {


    var uri = "http://127.0.0.1:5000/ss/v1.0/contact";
    var info = $('form').serializeArray();
    var subject = info[0].value;
    var bodyMessage = info[1].value;
    var dataToSend = {
        "subject": subject,
        "bodyMessage": bodyMessage
    }

    var data = post(uri, dataToSend);
    if (data.success) {
        // check if user is logged in
        if (isLoggedIn == true) {
            
            alert(data.response[0].dispSub);
            dispSub = data.response[0].dispSub;
            alert(dispSub);
            
        }
        else {
            alert("You need to be logged in to use this feature.");
        }
        
        window.location.assign("account.html");
        
    } else {
        alert(data.responseJSON.response);
    }
    /*
        $.post({
            url: uri,
            contentType: "application/json",
            dataType: 'json',
            data: JSON.stringify(dataToSend),
            success: function(data) {
                isLoggedIn = true;
                alert(data.response[0].dispName);
                dispName = data.response[0].dispName;
                alert(dispName);
                window.location.assign("account.html");
                //loadAccountPage();
            },
            error: function(data) {
                alert(data.responseJSON.response);
            }
        });
        */
}

function loadAccountPage() {
    console.log(dispName);
    $welcomeDisp.text("Welcome " + dispName);
}