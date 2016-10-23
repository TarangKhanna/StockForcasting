
// CHART BY MIKE BOSTOCK //
// I'll use this to test data and learn about d3 //
// eventually I will replace with my own implementation //

var svg = d3.select("#chart2 > svg"),
    margin = {top: 20, right: 50, bottom: 30, left: 50},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom,
    g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var parseTime = d3.timeParse("%d-%b-%y");

var x = d3.scaleTime()
    .rangeRound([0, width]);

var y = d3.scaleLinear()
    .rangeRound([height, 0]);

var line = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.close); });

d3.tsv("data2.tsv", function(d) {
  d.date = parseTime(d.date);
  d.close = +d.close;
  return d;
}, function(error, data) {
  if (error) throw error;

  x.domain(d3.extent(data, function(d) { return d.date; }));
  y.domain(d3.extent(data, function(d) { return d.close; }));

  g.append("g")
      .attr("class", "axis axis--x")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

  g.append("g")
      .attr("class", "axis axis--y")
      .call(d3.axisLeft(y))
    .append("text")
      .attr("fill", "#000")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "0.71em")
      .style("text-anchor", "end")
      .text("Price ($)");

  g.append("path")
      .datum(data)
      .attr("class", "line")
      .attr("d", line);
});
//////////////////////////////////////////////////////////////

// RESIZE CHART
var chart1 = $("#chart1 > #chart"),
    aspect = chart1.width() / chart1.height(),
    container = chart1.parent();
$(window).on("resize", function() {
    var targetWidth = container.width();
    chart1.attr("width", targetWidth);
    chart1.attr("height", Math.round(targetWidth / aspect));
}).trigger("resize");

var chart2 = $("#chart2 > #chart"),
    aspect = chart2.width() / chart2.height(),
    container = chart2.parent();
$(window).on("resize", function() {
    var targetWidth = container.width();
    chart2.attr("width", targetWidth);
    chart2.attr("height", Math.round(targetWidth / aspect));
}).trigger("resize"); 

//////////////////////////////////////////////////////////////