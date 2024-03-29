var $parag;
var dispName;
var userID;
var $welcomeDisp;
var isLoggedIn = false;

$(document).ready(function() {
    // On ready things
    // Also gets run when the login modal is closed

    // Page specific js

    if (document.title == "StockStokr - Home") {
        dispName = localStorage['firstName'] || 'User';
        userID = localStorage['UID'] || '-1';
        $parag = $("#parag");
    }
    if (document.title == "StockStokr - Account") {
        $welcomeDisp = $("#welcomeDisp");
        loadAccountPage();
    }
});

// function Post(yourUrl, dataToSend){
//     var xmlhttp = new XMLHttpRequest(); // a new request
//     xmlhttp.open("POST", yourUrl);
//     xmlhttp.setRequestHeader("Content-Type", "application/json");
//     xmlhttp.send(dataToSend);
//     return xmlhttp.responseText;
// }

function closeModal() {
    $("#login").modal("toggle");
}

function populate_stocks(userID) {
    var uri2 = "http://10.186.53.39:5000/todo/api/v1.0/tasks/getStocks";

    var dataToSend = {
        "userID":userID
    }
    $.ajax({
        method: "POST",
        url: uri2,
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify(dataToSend),
        success: function(data) {
            save_cookies(data);
        },
        error: function(data) {
            // console.log(data);
            alert("An error occured.");
        }
    });
    return "populated stocks";
}

function tweeter_data(stock){
    var uri2 = "http://10.186.53.39:5000/todo/api/v1.0/tasks/getTweetdata";

    var dataToSend = {
        "stock":stock
    }
    $.ajax({
        method: "POST",
        url: uri2,
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify(dataToSend),
        success: function(data) {
            // localStorage
        },
        error: function(data) {
            // console.log(data);
            alert("An error occured.");
        }
    });
}

function save_cookies(stockInfo){
    var data = stockInfo.data;
    alert("data[i] "+data[0]);
    for(var i = 0; i <= data.length; i++){
        var index = 'stockWatch' + i;
        // tweeter_data(data[i]);
        localStorage[index] = data[i];
    }
}

function requestLogin() {

    alert("logging in");
    var uri = "http://10.186.53.39:5000/ss/v1.0/login";
    var info = $('form').serializeArray();
    var email = info[0].value;
    var pswd = info[1].value;
    var dataToSend = {
        "email": email,
        "pswd": pswd
    }

    $.ajax({
        type: 'POST',
        url: uri,
        contentType: "application/json",
        dataType: 'json',
        data: JSON.stringify(dataToSend),
        success: function(data) {
            // alert("in success")
            console.log(data);
            isLoggedIn = true;
            var status = data.status;
            var condition = 1;
            while(1) {
                if (status == 'loggedIN') {
                    localStorage['firstName'] = data.firstName;
                    localStorage['UID'] = data.userID;
                    status = populate_stocks(data.userID);
                    // window.location.assign("account.html");
                } else {
                    alert("wrong password, please retry");
                }
                if (status == "no stocks" || status == "populated") {
                    condition = 0;
                }
            }
        },
        error: function(data) {
            console.log(data);
            // alert("giving here");
        }

    });
    
}


function loadAccountPage() {
    dispName = localStorage['firstName'] || 'User';
    userID = localStorage['UID'] || 'UserID';
    loggedIN = true;
    $welcomeDisp.text("Welcome " + dispName);

}
