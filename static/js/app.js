// Store our API endpoint inside queryUrl
// Link to GeoJSON
var APILink = "/ee/co2";
//fetch(request, {mode: 'cors'});

// Creating map object
var myMap = L.map("map", {
  center: [30,  35],
  zoom: 2
});

// Adding tile layer
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets",
  accessToken: API_KEY
}).addTo(myMap);

var geojson;

// Grab data with d3
d3.json(APILink).then(function (data) {
  // Create a new choropleth layer
  geojson = L.choropleth(data, {

    // Define what  property in the features to use
    valueProperty: "2017",

    // Set color scale
    scale: ["#ffffb2", "#b10026"],

    // Number of breaks in step range
    steps: 10,

    // q for quartile, e for equidistant, k for k-means
    mode: "e",
    style: {
      // Border color
      color: "#fff",
      weight: 1,
      fillOpacity: 0.8
    },

    // Binding a pop-up to each layer
    onEachFeature: function (feature, layer) {
      layer.bindPopup(feature.properties.ADMIN + ", " + "<br>CO2 Emissions:<br>" + feature.properties['2017']);
    }
  }).addTo(myMap);

  // Set up the legend
  var legend = L.control({ position: "bottomright" });
  legend.onAdd = function () {
    var div = L.DomUtil.create("div", "info legend");
    var limits = geojson.options.limits;
    var colors = geojson.options.colors;
    var labels = [];

    // Add min & max
    var legendInfo = "<h1>CO2 Emissions (MtCO2)</h1>" +
      "<div class=\"labels\">" +
      "<div class=\"min\">" + limits[0] + "</div>" +
      "<div class=\"max\">" + limits[limits.length - 1] + "</div>" +
      "</div>";

    div.innerHTML = legendInfo;

    limits.forEach(function (limit, index) {
      labels.push("<li style=\"background-color: " + colors[index] + "\"></li>");
    });

    div.innerHTML += "<ul>" + labels.join("") + "</ul>";
    return div;
  };

  // Adding legend to the map
  legend.addTo(myMap);

});

$(function () {
  $('#container').highcharts({
  chart: {
      plotBackgroundColor: null,
      plotBorderWidth: null,
      plotShadow: false,
      type: 'pie'
  },
  title: {
      text: 'Change in Share of Renewables in Electricity Production (2000 -2017)'
  },
  tooltip: {
      pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
  },
  plotOptions: {
      pie: {
          allowPointSelect: true,
          cursor: 'pointer',
          dataLabels: {
              enabled: false
          },
          showInLegend: true
      }
  },
  series: [{
      name: 'Renewable Energy Change',
      colorByPoint: true,
      data: [{
          name: 'Germany',
          y: 27.10,
          sliced: true,
          selected: true
      }, {
          name: 'United Kingdom',
          y: 26.80
      }, {
          name: 'Belgium',
          y: 15.90
      }, {
          name: 'Spain',
          y: 15.20
      }, {
          name: 'Italy',
          y: 14.90
      }, {
          name: 'Poland',
          y: 12.50
      }, {
          name: 'Netherlands',
          y: 11.50
      }, {
          name: 'Colombia',
          y: 11.30
      }, {
          name: 'Romania',
          y: 10.20
      }, {
          name: 'New Zealand',
          y: 9.90
      }]
  }]
})
});
