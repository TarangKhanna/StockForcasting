var message = '';

var company = 'Company';
var currentPrice = '0.00';
var projected = '0.00';
var buyorsell = 'unch';
var userID = localStorage['UID']||'-1';
// alert("In browse");
var i = 0;
while (1) {
    var name = "stockWatch" + i;
    var watchlisted = localStorage[name]||"default";
    // alert(watchlisted);
    if (watchlisted == "default") {
        if (i == 0) {
            message = '<div class="window"><h4>There is currently nothing in your watchlist.</h4>Add stocks to your watchlist from "Browse" or "Home" to see them here.</div>';
            document.write(message);
        }
        break;
    }
    else {
        if (watchlisted == "GOOGL") {
    
            currentPrice = '780.88';
            projected = '762.52';
            buyorsell = 'Sell'; 
            message = '<div class="window"> <h3 style="margin-left: 25px;">Google Inc.</h3> <button type="button" style="margin-right: 25px;" onClick="stock_update(\'' + watchlisted + '\')">Update Stock</button> <h4 style="text-align: center; padding-bottom: 25px; padding-top: 25px;"> -- Projected Closing Stock Price -- </h4> <div id="chart1"> <style> /* set the CSS */ .line { fill: none; stroke: url(#line-gradient); stroke-width: 2px; } </style> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="lgraph.js"></script> </div> <h4 style="text-align: center; padding-bottom: 25px; padding-top: 50px;"> -- Numerical and Qualitative Analysis -- </h4> <div class="row"> <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12"> <table class="table table-responsive"> <thead> <tr> <th>Stock Name</th> <th>Google Inc.</th> </tr> </thead> <tbody> <tr> <td>Suggested Action</td> <td>' + buyorsell + '</td> </tr> <tr> <td>Current Price</td> <td>' + currentPrice + '</td> </tr> <tr> <td>Projected Price </td> <td>' + projected + '</td> </tr> </tbody> </table> </div> <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12"> <div id="chart4"> <svg id="chart" width="450" height="250" viewBox="0 0 450 250" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="pgraph.js"></script> </div> </div> </div> <h4 style="text-align: center; padding-bottom: 25px; padding-top: 50px;"> -- Company History -- </h4> <div id="chart3"> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="hgraph.js"></script> </div> </div>';
            document.write(message);
        }
        if (watchlisted == "AAPL") {
            
            currentPrice = '109.62';
            projected = '110.28';
            buyorsell = 'Buy';
            message = '<div class="window"> <h3 style="margin-left: 25px;">Apple Inc.</h3> <button type="button" style="margin-right: 25px;" onClick="stock_update(\'' + watchlisted + '\')">Update Stock</button><h4 style="text-align: center; padding-bottom: 25px; padding-top: 25px;"> -- Projected Closing Stock Price -- </h4> <div id="chart2"> <style> /* set the CSS */ .line { fill: none; stroke: url(#line-gradient); stroke-width: 2px; } </style> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="lgraph2.js"></script> </div> <h4 style="text-align: center; padding-bottom: 25px; padding-top: 50px;"> -- Numerical and Qualitative Analysis -- </h4> <div class="row"> <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12"> <table class="table table-responsive"> <thead> <tr> <th>Stock Name</th> <th>Apple Inc.</th> </tr> </thead> <tbody> <tr> <td>Suggested Action</td> <td>' + buyorsell + '</td> </tr> <tr> <td>Current Price</td> <td>' + currentPrice + '</td> </tr> <tr> <td>Projected Price (1w)</td> <td>' + projected  + '</td> </tr> </tbody> </table> </div> <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12"> <div id="chart6"> <svg id="chart" width="450" height="250" viewBox="0 0 450 250" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="pgraph2.js"></script> </div> </div> </div> <h4 style="text-align: center; padding-bottom: 25px; padding-top: 50px;"> -- Company History -- </h4> <!-- CHART --> <div id="chart5"> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="hgraph2.js"></script> </div> </div>';
            document.write(message);
        }
        if (watchlisted == "IBM") {
            currentPrice = '159.56';
            projected = '158.80';
            buyorsell = 'Sell'; 
            message = '<div class="window"> <h3 style="margin-left: 25px;">IBM Inc.</h3> <button type="button" style="margin-right: 25px;" onClick="stock_update(\'' + watchlisted + '\')">Update Stock</button><h4 style="text-align: center; padding-bottom: 25px; padding-top: 25px;"> -- Projected Closing Stock Price -- </h4> <div id="chart7"> <style> /* set the CSS */ .line { fill: none; stroke: url(#line-gradient); stroke-width: 2px; } </style> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="lgraph3.js"></script> </div> <h4 style="text-align: center; padding-bottom: 25px; padding-top: 50px;"> -- Numerical and Qualitative Analysis -- </h4> <div class="row"> <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12"> <table class="table table-responsive"> <thead> <tr> <th>Stock Name</th> <th>IBM Inc.</th> </tr> </thead> <tbody> <tr> <td>Suggested Action</td> <td>' + buyorsell + '</td> </tr> <tr> <td>Current Price</td> <td>' + currentPrice + '</td> </tr> <tr> <td>Projected Price (1w)</td> <td>' + projected  + '</td> </tr> </tbody> </table> </div> <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12"> <div id="chart8"> <svg id="chart" width="450" height="250" viewBox="0 0 450 250" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="pgraph3.js"></script> </div> </div> </div> <h4 style="text-align: center; padding-bottom: 25px; padding-top: 50px;"> -- Company History -- </h4> <!-- CHART --> <div id="chart9"> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="hgraph3.js"></script> </div> </div>';
            document.write(message);
        } 
    }
    
    i++;
}



function stock_update(comp) {
    alert("Updating stock data for " + comp);
    var uri2 = "http://10.186.53.39:5000/todo/api/v1.0/tasks/getAIdata";

    var dataToSend = {
        "stock":comp,
        "days":10
    }
    $.ajax({
        method: "POST",
        url: uri2,
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify(dataToSend),
        success: function(data) {
            alert(comp + " data updated");
        },
        error: function(data) {
            // console.log(data);
            alert("An error occured.");
        }
    }); 
}
//Check if Google is in the watchlist
//if (0) {
//    message = '<div class="window"> <h3 style="margin-left: 25px;">Google Inc.</h3> <h4 style="text-align: center; padding-bottom: 25px; padding-top: 25px;"> -- Projected Closing Stock Price -- </h4> <div id="chart1"> <style> /* set the CSS */ .line { fill: none; stroke: url(#line-gradient); stroke-width: 2px; } </style> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="lgraph.js"></script> </div> <h4 style="text-align: center; padding-bottom: 25px; padding-top: 50px;"> -- Numerical and Qualitative Analysis -- </h4> <div class="row"> <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12"> <table class="table table-responsive"> <thead> <tr> <th>Stock Name</th> <th>Google Inc.</th> </tr> </thead> <tbody> <tr> <td>Suggested Action</td> <td>' + buyorsell + '</td> </tr> <tr> <td>Current Price</td> <td>' + currentPrice + '</td> </tr> <tr> <td>Projected Price </td> <td>' + projected + '</td> </tr> </tbody> </table> </div> <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12"> <div id="chart4"> <svg id="chart" width="450" height="250" viewBox="0 0 450 250" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="pgraph.js"></script> </div> </div> </div> <h4 style="text-align: center; padding-bottom: 25px; padding-top: 50px;"> -- Company History -- </h4> <div id="chart3"> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="hgraph.js"></script> </div> </div>';
//    document.write(message);
//}

// Check if Apple is in the watchlist
//if (0){
//    message = '<div class="window"> <h3 style="margin-left: 25px;">Apple Inc.</h3> <h4 style="text-align: center; padding-bottom: 25px; padding-top: 25px;"> -- Projected Closing Stock Price -- </h4> <div id="chart2"> <style> /* set the CSS */ .line { fill: none; stroke: url(#line-gradient); stroke-width: 2px; } </style> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="lgraph2.js"></script> </div> <h4 style="text-align: center; padding-bottom: 25px; padding-top: 50px;"> -- Numerical and Qualitative Analysis -- </h4> <div class="row"> <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12"> <table class="table table-responsive"> <thead> <tr> <th>Stock Name</th> <th>Apple Inc.</th> </tr> </thead> <tbody> <tr> <td>Suggested Action</td> <td>' + buyorsell + '</td> </tr> <tr> <td>Current Price</td> <td>' + currentPrice + '</td> </tr> <tr> <td>Projected Price (1w)</td> <td>' + projected  + '</td> </tr> </tbody> </table> </div> <div class="col-lg-6 col-md-6 col-sm-12 col-xs-12"> <div id="chart6"> <svg id="chart" width="450" height="250" viewBox="0 0 450 250" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="pgraph2.js"></script> </div> </div> </div> <h4 style="text-align: center; padding-bottom: 25px; padding-top: 50px;"> -- Company History -- </h4> <!-- CHART --> <div id="chart5"> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="hgraph2.js"></script> </div> </div>';
//    document.write(message);
//}

// If nothing is in the watchlist
//if (message == '') {
//    message = '<div class="window"><h4>There is currently nothing in your watchlist.</h4>Add stocks to your watchlist from "Browse" or "Home" to see them here.</div>';
//    document.write(message);
//}

    