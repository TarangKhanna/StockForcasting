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

function Post(yourUrl, dataToSend){
    var xmlhttp = new XMLHttpRequest(); // a new request
    xmlhttp.open("POST", yourUrl);
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlhttp.send(dataToSend);
    return xmlhttp.responseText;          
}

function closeModal() {
    $("#login").modal("toggle");
}

function requestLogin() {

    alert("logging in");
    var uri = "https://10.186.57.168:5000/ss/v1.0/login";
    var info = $('form').serializeArray();
    //console.log(info);
    var email = info[0].value;
    var pswd = info[1].value;
    var dataToSend = {
        "email": email,
        "pswd": pswd
    }
    
    data: JSON.stringify(dataToSend),
    alert("now sending data");
    json_response = JSON.parse(Post(uri, dataToSend));
    if(json_response['logged in'] == "Logged IN") {
        alert('logged in ');
        window.location.assign("account.html");
    }
    else {
        alert("wrong password");
    }

    // $.post({
    //     url: uri,
    //     dataType: 'json',
    //     contentType: "application/json",
    //     data: JSON.stringify(dataToSend),
    //     success: function(data) {
    //         console.log(data);
    //         isLoggedIn = true;
    //         alert("in success");
    //         dispName = data.response[0].firstName;
    //         alert(dispName);
    //         window.location.assign("account.html");
    //     },
    //     error: function(data) {
    //         console.log(data);
    //         alert("giving here");
    //     }
    // });
}

function loadAccountPage() {
    //console.log(dispName);
    $welcomeDisp.text("Welcome " + dispName);

}
