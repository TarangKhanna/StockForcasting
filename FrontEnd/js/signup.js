$signupForm;

$(document).ready(function() {

    $signupForm = $("#signupForm");

});

function signup() {
    var uri = "http://127.0.0.1:5000/ss/v1.0/login";
    var info = $('form').serializeArray();
    var uname = info[0].value;
    var pswd = info[1].value;
    var dataToSend = {
        "uname": uname,
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
            alert(dispName);
            window.location.assign("account.html");
            //loadAccountPage();
        },
        error: function(data) {
            alert(data.responseJSON.response);
        }
    });
}
