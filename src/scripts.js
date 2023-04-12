let mapOptions = {
  center:[51.958, 9.141],
  zoom:10
}

let map = new L.map('map' , mapOptions);

let layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
map.addLayer(layer);

let countClick = 0;
let marker = null;
let coordsArray = [];

// Google Maps Distance Matrix API key
const apiKey = 'AIzaSyB5UAh67qqEWkt8i2VH6AMD3KJgIdx4vNI';

function getDistanceFromLatLonInKm(lat1, lon1, lat2, lon2) {
  const url = `https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins=${lat1},${lon1}&destinations=${lat2},${lon2}&key=${apiKey}`;
  return fetch(url)
    .then(response => response.json())
    .then(data => data.rows[0].elements[0].distance.value / 1000)
    .catch(error => {
      console.error('Error fetching distance:', error);
      return null;
    });
}

map.on('click', async (event) => {
  if (marker !== null) {
    map.removeLayer(marker);
  }

  countClick += 1;
  marker = L.marker([event.latlng.lat, event.latlng.lng]).addTo(map);

  document.getElementById('latitude').value = event.latlng.lat;
  document.getElementById('longitude').value = event.latlng.lng;

  coordsArray.push([event.latlng.lat, event.latlng.lng]);

  if (coordsArray.length >= 2) {
    const distance = await getDistanceFromLatLonInKm(coordsArray[0][0], coordsArray[0][1], coordsArray[1][0], coordsArray[1][1]);
    if (distance !== null) {
      document.getElementById('distance').innerHTML = `Distance: ${distance} km`;
    }
  }
});

// Save the array to a text file on button click
const saveButton = document.getElementById('saveButton');
saveButton.addEventListener('click', () => {
  const coordsData = coordsArray.map(coords => coords.join(',')).join('\n');
  const file = new Blob([coordsData], {type: 'text/plain'});

  // Create a link to download the file
  const downloadLink = document.createElement('a');
  downloadLink.href = URL.createObjectURL(file);
  downloadLink.download = 'coordinates.txt';
  document.body.appendChild(downloadLink);

  // Click the link to download the file
  downloadLink.click();
  document.body.removeChild(downloadLink);

  // Define the start and end points
  const lat1 = coordsArray[0][0];
  const lng1 = coordsArray[0][1];
  const lat2 = coordsArray[1][0];
  const lng2 = coordsArray[1][1];

  // Set up the Google Maps Roads API client
  const roadsAPI = new google.maps.RoadsService();

  // Check if there is a road between the start and end points
  const startPoint = new google.maps.LatLng(lat1, lng1);
  const endPoint = new google.maps.LatLng(lat2, lng2);
  roadsAPI.nearestRoads({points: [startPoint, endPoint]}, (response, status) => {
    if (status !== 'OK') {
      console.error('Error:', status);
      return;
      }
      
      // Check if the start and end points are snapped to the same road segment
      const startSnapped = response.snappedPoints[0];
      const endSnapped = response.snappedPoints[1];
      if (startSnapped.placeId === endSnapped.placeId) {
      console.log('The two points are connected by road.');
      } else {
      console.log('The two points are not connected by road.');
      }
  });
});
