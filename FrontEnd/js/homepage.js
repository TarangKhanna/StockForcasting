function split() {
    var userID = localStorage['UID']||'-1'; 
    
    if (userID == -1) {
        window.location.href = "index.html";
    }
    else {
        window.location.href = "account.html";
    }
}