// Store our API endpoint inside queryUrl
var queryUrl = "/ee/gas"
//gas data
d3.json(queryUrl, function (data) {
  file = '../data/countries.geojson';

  d3.json(file).then(countryPolygons => {
    console.log(countryPolygons);
    L.geojson(countryPolygons);
  });


  
  // Once we get a response, send the data.features object to the createFeatures function
  createFeatures(data.features);
});





// function createFeatures(earthquakeData) {

//   // Define a function we want to run once for each feature in the features array
//   // Give each feature a popup describing the place and time of the earthquake
//   function onEachFeature(feature, layer) {
//     layer.bindPopup("<h3>Location: " + feature.properties.place +
//       "</h3><hr><p>Magnitude: " + (feature.properties.mag) + "</p>");
//   }

//     // Conditionals for countries points

//   function color(mag) {
//     if (mag < 1) {return "#ffffb2"}
//     else if  (mag < 2) {return "#fed976"}
//     else if (mag < 3) {return "#feb24c"}
//     else if (mag < 4) {return "#fd8d3c"}
//     else if (mag < 5) {return "#f03b20"}
//     else {return "#bd0026"}
//     //color schemes: http://colorbrewer2.org/#type=sequential&scheme=YlOrRd&n=6
//   };
//   // Create a GeoJSON layer containing the features array on the earthquakeData object
//   // Run the onEachFeature function once for each piece of data in the array
//   var earthquakes = L.geoJSON(earthquakeData, {
//     pointToLayer: function(feature, loc) {
//       var geojsonMarkerOptions = {
//         radius: 4.75 * feature.properties.mag,
//         fillColor: color(feature.properties.mag),
//         weight: 1,
//         opacity: 1,
//         fillOpacity: 0.76
//       };
//       return L.circleMarker(loc, geojsonMarkerOptions);
//     },
//     onEachFeature: onEachFeature
//   });

//   // Sending our earthquakes layer to the createMap function
//   createMap(earthquakes);
// }

// function createMap(earthquakes) {

//   // Define streetmap and darkmap layers
//   var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
//     attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
//     maxZoom: 18,
//     id: "mapbox.streets",
//     accessToken: API_KEY
//   });

//   // Define a baseMaps object to hold our base layers
//   var baseMaps = {
//     "Street Map": streetmap,
//   };

//   // Create overlay object to hold our overlay layer
//   var overlayMaps = {
//     Earthquakes: earthquakes
//   };

//   // Create our map, giving it the streetmap and earthquakes layers to display on load
//   var myMap = L.map("map", {
//     center: [
//       33.38, -97.99
//     ],
//     zoom: 4,
//     layers: [streetmap, earthquakes]
//   });

//   // Create a layer control
//   // Pass in our baseMaps and overlayMaps
//   // Add the layer control to the map
//   L.control.layers(baseMaps, overlayMaps, {
//     collapsed: false
//   }).addTo(myMap);


}