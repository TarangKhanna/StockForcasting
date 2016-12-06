company = 'IBM';
//Prints IBM lgraph3 (predicted)
if (1){
    message = '<div class="row"> <div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"> <div class="window"> <div class="dropdown"> <button type="button" class="btn btn-block dropdown-toggle" data-toggle="dropdown" style="padding: 0px; margin-bottom: 5px;"> <table class="table table-responsive"> <thead> <tr> <th>Stock Name</th> <th>Current Price</th> <th>Projected Price</th> </tr> </thead> <tbody> <tr> <td>IBM Inc.</td> <td>' + currentPrice + '</td> <td>' + projected + '</td> </tr> </tbody> </table> <figure> <div id="chart7"> <!-- CHART --> <style> /* set the CSS */ .line { fill: none; stroke: url(#line-gradient); stroke-width: 2px; } </style> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="lgraph3.js"></script> </div> </figure> </button> <ul class="dropdown-menu dropdown-menu-center" onClick="addWatchlist(\'' + company + '\', \'' + userID + '\')"> <li style="background-color: #ffffff; text-align: center;"> <h4>Add IBM to Watchlist</h4> </li> </ul> </div> </div> </div>';
    document.write(message);
}

//Prints IBM pgraph3 
if (1) {
    message = '<div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"> <div class="window"> <div class="dropdown"> <button type="button" class="btn btn-block dropdown-toggle" data-toggle="dropdown" style="padding: 0px; margin-bottom: 5px;"> <table class="table table-responsive"> <thead> <tr> <th>Stock Name</th> <th>Current Price</th> <th>Suggested Action</th> </tr> </thead> <tbody> <tr> <td>IBM Inc.</td> <td>' + currentPrice + '</td> <td>' + buyorsell + '</td> </tr> </tbody> </table> <figure> <div id="chart8"> <!-- CHART --> <svg id="chart" width="450" height="250" viewBox="0 0 450 250" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="pgraph3.js"></script> </div> </figure> </button> <ul class="dropdown-menu dropdown-menu-center" onClick="addWatchlist(\'' + company + '\', \'' + userID + '\')"> <li style="background-color: #ffffff; text-align: center;"> <h4>Add Google to Watchlist</h4> </li> </ul> </div> </div> </div>';
    document.write(message);
}


//Prints IBM hgraph3 (history)
if (1){
    message = '<div class="col-lg-4 col-md-4 col-sm-6 col-xs-12"> <div class="window"> <div class="dropdown"> <button type="button" class="btn btn-block dropdown-toggle" data-toggle="dropdown" style="padding: 0px; margin-bottom: 5px;"> <table class="table table-responsive"> <thead> <tr> <th>Stock Name</th> <th>Current Price</th> <th>Projected Price</th> </tr> </thead> <tbody> <tr> <td>IBM Inc.</td> <td>' + currentPrice + '</td> <td>' + projected + '</td> </tr> </tbody> </table> <figure> <div id="chart9"> <!-- CHART --> <svg id="chart" width="900" height="500" viewBox="0 0 900 500" preserveAspectRatio="xMidYMid meet"> </svg> <script src="https://d3js.org/d3.v4.min.js"></script> <script src="hgraph3.js"></script> </div> </figure> </button> <ul class="dropdown-menu dropdown-menu-center" onClick="addWatchlist(\'' + company + '\', \'' + userID + '\')"> <li style="background-color: #ffffff; text-align: center;"> <h4>Add IBM to Watchlist</h4> </li> </ul> </div> </div> </div> </div>';
    document.write(message);
}