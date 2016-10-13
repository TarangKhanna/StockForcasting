var $parag;

$(document).ready(function() {
    // On ready things
    // Also gets run when the login modal is closed
    $parag = $("#parag");
});


function requestLogin() {
    var uri = "http://127.0.0.1:5000/ss/v1.0/login";
    var info = $('form').serializeArray();
    var uname = info[0].value;
    var pswd = info[1].value;
    var dataToSend = {
            "uname": uname,
            "pswd": pswd
        }
        //alert(uname);
        //alert(pswd);

    $.post({
        url: uri,
        contentType: "application/json",
        dataType: 'json',
        data: JSON.stringify(dataToSend),
        complete: function(data) {
            alert("user name: " + data.responseJSON.username);
            console.log(data);
        }
    });
    /*
    .done(function(data) {
        alert("it worked!");
        alert(data);
    });
    */
}
