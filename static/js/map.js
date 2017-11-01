//map.js
//logic to display a map

(function(){
    'use strict';

    //reads in gexf file and renders in webpage
    sigma.parsers.gexf('/static/files/GeoLayout.gexf', {

      container: 'container'

    },
    function(s){


    }
  );
/*
  // Let's first initialize sigma:
  // first example of sigma
  // draws 2 nodes and a line.
var s = new sigma('container');

// Then, let's add some data to display:
s.graph.addNode({
  // Main attributes:
  id: 'n0',
  label: 'Hello',
  // Display attributes:
  x: 0,
  y: 0,
  size: 1,
  color: '#f00'
}).addNode({
  // Main attributes:
  id: 'n1',
  label: 'World !',
  // Display attributes:
  x: 1,
  y: 1,
  size: 1,
  color: '#00f'
}).addEdge({
  id: 'e0',
  // Reference extremities:
  source: 'n0',
  target: 'n1'
});

// Refresh the graph to see the changes:
// Finally, let's ask our sigma instance to refresh:
s.refresh();
*/
    /*
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
                console.log("lat", d.lat, "long", d.long)
              });
            } else {

            }
          });

        var source = "";
        var target = "";



        d3.csv("/static/js/SOAClimateMappingProject_Entities.csv", function(data) {
        //console.log(data[0]);
        source = data[0].Abr;
        target = data[1].Abr;
        console.log(source);
        console.log(target);
        });

        var width = 640;
        var height = 480;

        /*
        //hardcoded links
        var links = [
        { source: 'Tom', target: 'Jim'},
        { source: 'Jim', target: 'Jack'},
        { source: 'Jack', target: 'Tom'},
        ];


        var links = [
          { source: source, target: target },
        ]

        var nodes = {};

        //parse links to Nodes
        links.forEach(function(link){
            link.source = nodes[link.source] ||
              (nodes[link.source] = {name: link.source});
            link.target = nodes[link.target] ||
              (nodes[link.target] = {name: link.target});

        });

        //add the svg to body
        var svg = d3.select('body').append('svg')
          .attr('width', width)
          .attr('height', height);

        var force = d3.layout.force()
          .size([width, height])
          .nodes(d3.values(nodes))
          .links(links)
          .on("tick", tick) //make the visualization dynamic
          .linkDistance(200) //how far apart the nodes are
          .start(); // start the layout rendering

        var link = svg.selectAll('.link')
          .data(links)
          .enter().append('line') // append a line TODO: will need append a path
                                  // for curved lines
          .attr('class', 'link');

        var node = svg.selectAll('.node')
          .data(force.nodes())
          .enter().append('circle')
          .attr('class', 'node')
          .attr('r', width * 0.03); // specify the radius
                                    // TODO: will need to make this attr more
                                    // more dynamic

        function tick(e){ //e gives position (not used yet)

          node.attr('cx', function(d) {return d.x; })
            .attr('cy', function(d) {return d.y;})
            .call(force.drag); //allows to drag the visualization

          link.attr('x1', function(d) {return d.source.x; })
              .attr('y1', function(d) {return d.source.y; })
              .attr('x2', function(d) {return d.target.x; })
              .attr('y1', function(d) {return d.source.y; })

        }
        */
}());
