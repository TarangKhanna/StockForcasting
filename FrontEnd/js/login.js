$(document).ready(function() {
    // On ready things
    // Also gets run when the login modal is closed

    $("#loginform").click(function(e) {
        e.preventDefault();
        // ajax
        alert("this worked?");
        e.preventDefault();
    });
});


function requestLogin() {
    var uri = "http://http://127.0.0.1:5000/todo/api/v1.0/login/";
    var info = $('form').serializeArray();
    var uname = info[0].value;
    var pswd = info[1].value;
    //alert(uname);
    //alert(pswd);

    $.ajax({
        url: uri,
        //data: info,
        method: "GET"
    }).done(function(data) {
        alert("it worked!");
        alert(data);
    });
}
