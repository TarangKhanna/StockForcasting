
// set the dimensions and margins of the graph
var margin = {top: 20, right: 50, bottom: 30, left: 50},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

// parse the date / time
var parseTime = d3.timeParse("%Y-%m-%d");

// set the ranges
var x = d3.scaleTime().range([0, width]);
var y = d3.scaleLinear().range([height, 0]);

// define the line
var valueline = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.close); });

// append the svg obgect to the body of the page
// appends a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select("#chart3 > svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");

// Get the data
d3.csv("GOOGL_training.csv", function(error, data) {
  if (error) throw error;

  // format the data
  data.forEach(function(d) {
      d.date = parseTime(d.Date);
      d.close = +d['Adj. Close'];
  });

  // Scale the range of the data
  x.domain(
      d3.extent(data, function(d) { return d.date; })
    );
  y.domain([
      d3.min(data, function(d) { return d.close; }) - 10, 
      d3.max(data, function(d) { return d.close; })
  ]);

  // Add the valueline path.
  svg.append("path")
      .data([data])
      .attr("class", "line")
      .attr("d", valueline)
      .style("stroke", "black");

  // Add the X Axis
  svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

  // Add the Y Axis
  svg.append("g")
      .call(d3.axisLeft(y));

});


//////////////////////////////////////////////////////////////

// RESIZE CHART
//var chart1 = $("#chart1 > #chart"),
//    aspect = chart1.width() / chart1.height(),
//    container = chart1.parent();
//$(window).on("resize", function() {
//    var targetWidth = container.width();
//    chart1.attr("width", targetWidth);
//    chart1.attr("height", Math.round(targetWidth / aspect));
//}).trigger("resize"); 

var chart3 = $("#chart3 > #chart"),
    aspect = chart3.width() / chart3.height(),
    container = chart3.parent();
$(window).on("resize", function() {
    var targetWidth = container.width();
    chart3.attr("width", targetWidth);
    chart3.attr("height", Math.round(targetWidth / aspect));
}).trigger("resize"); 


//////////////////////////////////////////////////////////////