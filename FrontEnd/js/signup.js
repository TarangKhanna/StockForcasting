var $signupForm;

$(document).ready(function() {

    $signupForm = $("#signupForm");

});

function signup() {
    //  alert("here");
    var uri = "http://stockapi.duckdns.org:5000/todo/api/v1.0/tasks/addUser";
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
        break;
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
        alert(data)
        success: function(data) {
            window.location.assign("account.html");
        },
        error: function(data) {
            console.log(data);
            alert("An error occured.");
        }
    });

}
