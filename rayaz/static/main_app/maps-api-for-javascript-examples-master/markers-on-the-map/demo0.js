

/**
 * Adds markers to the map highlighting the locations of the captials of
 * France, Italy, Germany, Spain and the United Kingdom.
 *
 * @param  {H.Map} map      A HERE Map instance within the application
 */
function addMarkersToMap(map,mylist,mylist2) {
    var group = new H.map.Group();
    for (var i = 0; i < mylist.length; i++) {
      var parisMarker = new H.map.Marker({lat:mylist[i],  lng:mylist2[i]});
      map.addObject(parisMarker);
      group.addObjects([parisMarker]);

    }
    map.addObject(group);
    map.setViewBounds(group.getBounds());
  }

function iconTest(map) {
  var icon = new H.map.Icon('/Users/vagif/Downloads/Masa.az/rayaz/static/main_app/images/mapmarker.png');
  var marker = new H.map.Marker({ lat: 52.5, lng: 13.4 }, { icon: icon });
  map.addObject(marker);
}


  /**
   * Boilerplate map initialization code starts below:
   */

  //Step 1: initialize communication with the platform
  // In your own code, replace variable app_id with your own app_id
  // and app_code with your own app_code
  var platform = new H.service.Platform({
    app_id: '9i5wRuB2qSMk4QXNsHJF',
    app_code: 'jqCkp-06H39jgB7IuENe3Q',
    useCIT: true,
    useHTTPS: true
  });
  var defaultLayers = platform.createDefaultLayers();

  //Step 2: initialize a map - this map is centered over Europe
  var map = new H.Map(document.getElementById('map'),
    defaultLayers.normal.map,{
    center: {lat:10.143105, lng:20.576927},
    zoom: 4
  });


  // add a resize listener to make sure that the map occupies the whole container
  window.addEventListener('resize', () => map.getViewPort().resize());

  //Step 3: make the map interactive
  // MapEvents enables the event system
  // Behavior implements default interactions for pan/zoom (also on mobile touch environments)
  var behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));

  // Create the default UI components
  var ui = H.ui.UI.createDefault(map, defaultLayers);

  var mine = [];
  var mine2 = [];

  function obtain(callback,encoded) {
    $.ajax({
      url: location.protocol + '//nominatim.openstreetmap.org/search?format=json&q='+String(encoded),
      async: false,
      success: callback
    });
  }
  function myCallback(data) {
    mine.push(data[0].lat);
    mine2.push(data[0].lon);
  }
  // Now use the map as required...
  $(document).ready(function() {
    var addresses = $('.yoyo');
    function logic() {
      for (var i = 0; i < addresses.length; i++) {
        var address = $('.yoyo').eq(i).text()
        var encoded = encodeURIComponent(address)
        obtain(myCallback,encoded);
      }
    }
    logic();
    addMarkersToMap(map,mine,mine2);
    iconTest(map);

  });
