// Store our API endpoint inside queryUrl
var queryUrl = "https://herokuenergyevolution.herokuapp.com/ee/solar_wind";
fetch(request, {mode: 'cors'});

d3.json(queryUrl).then(function(data) {
 // Once we get a response, send the data.features object to the createFeatures function
 //createFeatures(data.features);
 console.log(data);

});