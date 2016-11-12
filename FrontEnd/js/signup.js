var $signupForm;

$(document).ready(function() {

    $signupForm = $("#signupForm");

});

function signup() {
    //  alert("here");
    var uri = "http://127.0.0.1:5000/todo/api/v1.0/tasks";
    var info = $('form').serializeArray();
    var email = ($("#email")[0].value);
    var pwd = ($("#pwd")[0].value);
    var cpwd = ($("#cpwd")[0].value);
    var phone = ($("#phone")[0].value);
    var fname = ($("#fname")[0].value);
    var lname = ($("#lname")[0].value);

    if (pwd != cpwd) {
        alert("Passwords do not match.");
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
        method: "ADDUSER",
        contentType: "application/json",
        dataType: "json",
        headers: {
            "Access-Control-Allow-Headers": "Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers",
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "ADDUSER"
        },
        data: JSON.stringify(dataToSend),
        success: function(data) {
            dispName = data.response[0].dispName;
            window.location.assign("account.html");
        },
        error: function(data) {
            alert(data.responseJSON.response);
        }
    });

}
