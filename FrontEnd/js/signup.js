$signupForm;

$(document).ready(function() {

    $signupForm = $("#signupForm");

});

function signup() {
    var uri = "http://127.0.0.1:5000/ss/v1.0/login";
    var info = $('form').serializeArray();

    var dataToSend = {
        "uname": uname,
        "pswd": pswd
    }

    var data = post(uri, dataToSend);
}
