function initialize(locations, latState, lonState) {
    var mapOptions = {
        zoom: 5,
        center:  new google.maps.LatLng(latState, lonState)
    }
    var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    for (var i = 0; i < locations.length; i++){
          marker = new google.maps.Marker({
          position: new google.maps.LatLng(locations[i][0], locations[i][1]),
          map: map,
          title: locations[i][2]
      });
    }
}