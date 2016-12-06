var message = '';

var company = 'Company';
var currentPrice = '0.00';
var projected = '0.00';
var buyorsell = 'unch';
var userID = localStorage['UID']||'-1';

//Prints GOOGLE lgraph (predicted)
if (1) {
    message = '<div class="row"><div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"> <div class="window"> <div class="dropdown"> <button type="button" class="btn btn-block dropdown-toggle" data-toggle="dropdown" style="padding: 0px; margin-bottom: 5px;"> <table class="table table-responsive"> <thead> <tr> <th>Stock Name</th> <th>Current Price</th> <th>Projected Price</th> </tr> </thead> <tbody> <tr> <td>Google Inc.</td> <td>' + currentPrice + '</td> <td>' + projected + '</td> </tr> </tbody> </table> <figure> <div id="chart1"> <!-- CHART --> <style> /* set the CSS */ .line { fill: none; stroke: url(#line-gradient); stroke-width: 2px; } </style> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="lgraph.js"></script> </div> </figure> </button> <ul class="dropdown-menu dropdown-menu-center" onClick="addWatchlist(\'' + company + '\', \'' + userID + '\')"> <li style="background-color: #ffffff; text-align: center;"> <h4>Add Google to Watchlist</h4> </li> </ul> </div> </div> </div>';
    document.write(message);
}

//Prints APPLE lgraph2 (predicted)
if (1){
    message = '<div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"> <div class="window"> <div class="dropdown"> <button type="button" class="btn btn-block dropdown-toggle" data-toggle="dropdown" style="padding: 0px; margin-bottom: 5px;"> <table class="table table-responsive"> <thead> <tr> <th>Stock Name</th> <th>Current Price</th> <th>Projected Price</th> </tr> </thead> <tbody> <tr> <td>Apple Inc.</td> <td>' + currentPrice + '</td> <td>' + projected + '</td> </tr> </tbody> </table> <figure> <div id="chart2"> <!-- CHART --> <style> /* set the CSS */ .line { fill: none; stroke: url(#line-gradient); stroke-width: 2px; } </style> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="lgraph2.js"></script> </div> </figure> </button> <ul class="dropdown-menu dropdown-menu-center" onClick="addWatchlist(\'' + company + '\', \'' + userID + '\')"> <li style="background-color: #ffffff; text-align: center;"> <h4>Add Apple to Watchlist</h4> </li> </ul> </div> </div> </div>';
    document.write(message);
}

//Prints GOOGLE pgraph 
if (1) {
    message = '<div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"> <div class="window"> <div class="dropdown"> <button type="button" class="btn btn-block dropdown-toggle" data-toggle="dropdown" style="padding: 0px; margin-bottom: 5px;"> <table class="table table-responsive"> <thead> <tr> <th>Stock Name</th> <th>Current Price</th> <th>Suggested Action</th> </tr> </thead> <tbody> <tr> <td>Google Inc.</td> <td>' + currentPrice + '</td> <td>' + buyorsell + '</td> </tr> </tbody> </table> <figure> <div id="chart4"> <!-- CHART --> <svg id="chart" width="450" height="250" viewBox="0 0 450 250" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="pgraph.js"></script> </div> </figure> </button> <ul class="dropdown-menu dropdown-menu-center" onClick="addWatchlist(\'' + company + '\', \'' + userID + '\')"> <li style="background-color: #ffffff; text-align: center;"> <h4>Add Google to Watchlist</h4> </li> </ul> </div> </div> </div></div>';
    document.write(message);
}

//Prints APPLE pgraph2
if (1){
    message = '<div class="row"> <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"> <div class="window"> <div class="dropdown"> <button type="button" class="btn btn-block dropdown-toggle" data-toggle="dropdown" style="padding: 0px; margin-bottom: 5px;"> <table class="table table-responsive"> <thead> <tr> <th>Stock Name</th> <th>Current Price</th> <th>Suggested Action</th> </tr> </thead> <tbody> <tr> <td>Apple Inc.</td> <td>' + currentPrice + '</td> <td>' + buyorsell + '</td> </tr> </tbody> </table> <figure> <div id="chart6"> <!-- CHART --> <svg id="chart" width="450" height="250" viewBox="0 0 450 250" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="pgraph2.js"></script> </div> </figure> </button> <ul class="dropdown-menu dropdown-menu-center" onClick="addWatchlist(\'' + company + '\', \'' + userID + '\')"> <li style="background-color: #ffffff; text-align: center;"> <h4>Add Apple to Watchlist</h4> </li> </ul> </div> </div> </div>';
    document.write(message);
}

//Prints GOOGLE hgraph (history)
if (1) {
    message = '<div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"> <div class="window"> <div class="dropdown"> <button type="button" class="btn btn-block dropdown-toggle" data-toggle="dropdown" style="padding: 0px; margin-bottom: 5px;"> <table class="table table-responsive"> <thead> <tr> <th>Stock Name</th> <th>Current Price</th> <th>Projected Price</th> </tr> </thead> <tbody> <tr> <td>Google Inc.</td> <td>' + currentPrice + '</td> <td>' + projected + '</td> </tr> </tbody> </table> <figure> <div id="chart3"> <!-- CHART --> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="hgraph.js"></script> </div> </figure> </button> <ul class="dropdown-menu dropdown-menu-center" onClick="addWatchlist(\'' + company + '\', \'' + userID + '\')"> <li style="background-color: #ffffff; text-align: center;"> <h4>Add Google to Watchlist</h4> </li> </ul> </div> </div> </div>';
    document.write(message);
}

//Prints APPLE hgraph2 (history)
if (1){
    message = '<div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"> <div class="window"> <div class="dropdown"> <button type="button" class="btn btn-block dropdown-toggle" data-toggle="dropdown" style="padding: 0px; margin-bottom: 5px;"> <table class="table table-responsive"> <thead> <tr> <th>Stock Name</th> <th>Current Price</th> <th>Projected Price</th> </tr> </thead> <tbody> <tr> <td>Apple Inc.</td> <td>' + currentPrice + '</td> <td>' + projected + '</td> </tr> </tbody> </table> <figure> <div id="chart5"> <!-- CHART --> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="hgraph2.js"></script> </div> </figure> </button> <ul class="dropdown-menu dropdown-menu-center" onClick="addWatchlist(\'' + company + '\', \'' + userID + '\')"> <li style="background-color: #ffffff; text-align: center;"> <h4>Add Apple to Watchlist</h4> </li> </ul> </div> </div> </div>';
    document.write(message);
}

// If nothing is in the watchlist
if (0) {
    message = '<div class="window"><h4>There is currently nothing in your watchlist.</h4>Add stocks to your watchlist from "Browse" or "Home" to see them here.</div>';
    document.write(message);
}

function addWatchlist(comp, userID) {

    if(userID == "-1") {
    	alert("broken userID");
      return;
    }
    // alert("Added " + comp + " to watchlist");
    var uri = "http://10.186.57.168:5000/todo/api/v1.0/tasks/addStocks";

    dataToSend = {
    	'userID': userID,
    	'stockSymbol': comp
    }

    $.ajax({
        type: 'POST',
        url: uri,
        contentType: "application/json",
        dataType: 'json',
        data: JSON.stringify(dataToSend),
        success: function(data) {
            console.log(data);
            alert("stock " + comp + "added")
        },
        error: function(data) {
            console.log(data);
            alert("stock adding failed")
        }
    });

}