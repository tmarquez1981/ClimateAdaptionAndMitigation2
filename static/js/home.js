$(document).ready(function(){

  $('button').on('click', function(){
    $('#about').toggle();
  });
});


/*
(function(){
  'use strict';

  //variables for lat and long
  var lat = [];
  var long = [];
  var index = 0; //keeps track of index of arrays

  //pulls long and lat from csv file
  d3.csv("/static/js/SOAClimateMappingProject_Entities.csv")
        .row(function(d) {
          return {
            lat: +d.Lat,
            long: +d.Lng,
          };
        })
        .get(function(error, csv) {
          if (!error) {
            csv.forEach(function(d,i) {
              //console.log("lat", d.lat, "long", d.long)
              lat[0] = d.lat;
              //long[index] = d.long;
              //index++;
            });
          } else {

          }
        });

  console.log(lat);


  //below draws a map of the world
  var width = 960;
  var height = 400;

  var svg = d3.select("body").append("svg")

  var projection = d3.geo.mercator()
    .scale(width / 2 / Math.PI)
    //.scale(100)
    .translate([width / 2, height / 2])

   var path = d3.geo.path()
    .projection(projection);

    var url = "http://enjalot.github.io/wwsd/data/world/world-110m.geojson";
    d3.json(url, function(err, geojson) {
      svg.append("path")
      .attr("d", path(geojson))
    })


}());
*/
