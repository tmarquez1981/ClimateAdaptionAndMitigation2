//Map using google maps API
(function(){

  /*
  var queryset = document.getElementById('queryset');
  var myDjangoList = (queryset.replace(/&(l|g|quo)t;/g, function(a,b){
            return {
                l   : '<',
                g   : '>',
                quo : '"'
            }[b];
        }));

myDjangoList = myDjangoList.replace(/u'/g, '\'')
myDjangoList = myDjangoList.replace(/'/g, '\"')

myData = JSON.parse( myDjangoList );
*/
  //var queryset = document.getElementById('queryset');
  var queryset = "{{ queryset }}";
  //var data = JSON.parse(queryset);
  var data = queryset;
  console.log(data);

  //where the map is centered
  var position = {lat: 61.2181, lng: -149.9003};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: position
  });

  //array of markers
  var markers = [
    {
      coords:{lat:61.2181,lng:-149.9003},
      iconImage:'',
      content:'<h3>Some content here</h3>'
    }
  ];

  //loop through markers
  for(var i = 0; i < markers.length; i++){
    addMarker(markers[i]);
  }

  // add marker function
  // for adding multiple markers
  // anch, ak lat/lng: lat:61.2181, lng:-149.9003
  function addMarker(props){
    var marker = new google.maps.Marker({
      position:props.coords,
      map:map
      //icon:'some link to new icon' (add comma after map when adding)
    });

    //check for custom icon
    if(props.iconImage){
      //set icon image
      marker.setIcon(props.iconImage)
    }

    //check for content
    if(props.content){
      var infoWindow = new google.maps.InfoWindow({
        content: props.content
      });

      //event listener
      marker.addListener('click', function(){
        infoWindow.open(map, marker);
      });
    }
  }

/*
    var uluru = {lat: -25.363, lng: 131.044};
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: uluru
    });
    var marker = new google.maps.Marker({
      position: uluru,
      map: map
    });
    */
}());
