
// set the dimensions and margins of the graph
var margin = {top: 20, right: 50, bottom: 30, left: 50},
    width = 450 - margin.left - margin.right,
    height = 250 - margin.top - margin.bottom,
    radius = Math.min(width, height) / 2; 
    
// pass in three values here
var data = [41, 27, 32];
var name = ["Good", "Bad", "Neutral"];
var legendRectSize = 24;
var legendSpacing = 8;

var svg = d3.select("#chart6>svg")
    .datum(data)
    .datum(name)
    .attr("width", width)
    .attr("height", height)
  .append("g")
    .attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

var color = d3.scaleOrdinal()
    .range(["#6ced53", "#ff5d4f", "#ffff60"]);

var group = svg.append("g");

var arc = d3.arc()
    .innerRadius(0)
    .outerRadius(radius);

var pie = d3.pie();

var arcs = group.selectAll(".arc")
    .data(pie(data))
  .enter()
    .append("g")
    .attr("class", "arc");

arcs.append("path")
    .style("fill", function(d) { return color(d.data); })
    .transition().delay(function(d, i) { return 0; }).duration(1500)
    .attrTween('d', function(d) {
       var i = d3.interpolate(d.startAngle+0.1, d.endAngle);
       return function(t) {
           d.endAngle = i(t);
         return arc(d);
       }
  });

arcs.append("text")
    .attr("transform", function(d) { return "translate(" + arc.centroid(d) + ")"; })
    .attr("text-anchor", "middle")
    .attr("font-size", "1.5em")
    .text(function(d) { return d.name; });

var legend = svg.selectAll('.legend')                     
          .data(color.domain())                                   
          .enter()                                                
          .append('g')                                            
          .attr('class', 'legend')                                
          .attr('transform', function(d, i) {                     
            var height = legendRectSize + legendSpacing;          
            var offset =  height * color.domain().length / 2;     
            var horz = -2 * legendRectSize + 200;                       
            var vert = i * height - offset;                       
            return 'translate(' + horz + ',' + vert + ')';        
          });                                                     

        legend.append('rect')                                     
          .attr('width', legendRectSize)                          
          .attr('height', legendRectSize)                         
          .style('fill', color)                                   
          .style('stroke', color);                                

        legend.append('text')                                     
          .attr('x', legendRectSize + legendSpacing)              
          .attr('y', legendRectSize - legendSpacing)              
          .text(function(d) { return d; });


// RESIZE CHART
