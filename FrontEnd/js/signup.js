var $signupForm;

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

function signup() {
     // alert("here");

    var uri = "http://10.186.57.168:5000/todo/api/v1.0/tasks/addUser";
    var info = $('form').serializeArray();
    var email = ($("#email")[0].value);
    var pwd = ($("#pwd")[0].value);
    var cpwd = ($("#cpwd")[0].value);
    var phone = ($("#phone")[0].value);
    var fname = ($("#fname")[0].value);
    var lname = ($("#lname")[0].value);

    if (pwd != cpwd) {
        alert("Passwords do not match.");
        // signup();
        // break;
    }
    var dataToSend = {
        "firstName": fname,
        "lastName": lname,
        "age": "0",
        "phoneNumber": phone,
        "password": pwd,
        "email": email
    }
    $.ajax({
        url: uri,
        method: "POST",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify(dataToSend),
        success: function(data) {
            // alert("new user " + data.new_user[1]);
            localStorage['firstName'] = data.new_user[1];
            localStorage['UID'] = "" + data.new_user[0];
            window.location.assign("account.html");
        },
        error: function(data) {
            // console.log(data);
            alert("An error occured.");
        }
    });

}

function loadAccountPage() {
    dispName = localStorage['firstName'] || 'User';
    userID = localStorage['UID'] || 'UserID';
    loggedIN = true;
    $welcomeDisp.text("Welcome " + dispName);

}
