var message = '<div class="side-window"><h3 style="margin-left: 10px;"> Other Stocks to Consider </h3>';

var company = 'Company';
var currentPrice = '0.00';
var projected = '0.00';
var buyorsell = 'unch';

// create for loop that will iterate for every stock in our database

//Check if Google is in the watchlist
company = "Google Inc.";
//currentPrice = Google's latest price.
//projected = googles latest projected value.
buyorsell = "buy";

if (1) {
    message = message + '<div class = "dropdown"> <button type="button" class="btn btn-block dropdown-toggle" data-toggle="dropdown" style="padding: 0px; margin-bottom: 5px;"> <h3 style="text-align: left; margin-left: 10px;">' + company + '</h3> <h4 style="text-align: right; margin-right: 10px;"> Current Price: ' + currentPrice + ' </h4> <h4 style="text-align: right; margin-right: 10px;"> Projected: ' + projected + ' </h4> <h4 style="text-align: right; margin-right: 10px;"> ' + buyorsell + ' </h4> </button> <ul class="dropdown-menu dropdown-menu-right" onClick="addWatchlist()"> <li style="background-color: #ffffff; text-align: center;"> <h4>Add ' + company + ' to Watchlist</h4> </li> </ul> </div>';
}

//Check if Apple is in the watchlist
company = "Apple\ Inc.";
//currentPrice = Google's latest price.
//projected = googles latest projected value.
buyorsell = "buy";

if (1) {
    message = message + '<div class = "dropdown"> <button type="button" class="btn btn-block dropdown-toggle" data-toggle="dropdown" style="padding: 0px; margin-bottom: 5px;"> <h3 style="text-align: left; margin-left: 10px;">' + company + '</h3> <h4 style="text-align: right; margin-right: 10px;"> Current Price: ' + currentPrice + ' </h4> <h4 style="text-align: right; margin-right: 10px;"> Projected: ' + projected + ' </h4> <h4 style="text-align: right; margin-right: 10px;"> ' + buyorsell + ' </h4> </button> <ul class="dropdown-menu dropdown-menu-right" onClick="addWatchlist()"> <li style="background-color: #ffffff; text-align: center;"> <h4>Add ' + company + ' to Watchlist</h4> </li> </ul> </div>';
}

//Check if IBM is in the watchlist
//Check if Apple is in the watchlist
company = "IBM Inc.";
//currentPrice = Google's latest price.
//projected = googles latest projected value.
buyorsell = "buy";

if (1) {
    message = message + '<div class = "dropdown"> <button type="button" class="btn btn-block dropdown-toggle" data-toggle="dropdown" style="padding: 0px; margin-bottom: 5px;"> <h3 style="text-align: left; margin-left: 10px;">' + company + '</h3> <h4 style="text-align: right; margin-right: 10px;"> Current Price: ' + currentPrice + ' </h4> <h4 style="text-align: right; margin-right: 10px;"> Projected: ' + projected + ' </h4> <h4 style="text-align: right; margin-right: 10px;"> ' + buyorsell + ' </h4> </button> <ul class="dropdown-menu dropdown-menu-right" onClick="addWatchlist()"> <li style="background-color: #ffffff; text-align: center;"> <h4>Add ' + company + ' to Watchlist</h4> </li> </ul> </div>';
}

// If nothing is in the watchlist
if (message == '') {
    message = message + '<div class="window"><h4>No stocks available.</h4></div>';
}

message = message + '</div>';
document.write(message);

    

function addWatchlist() {
    alert("Added to watchlist");
}