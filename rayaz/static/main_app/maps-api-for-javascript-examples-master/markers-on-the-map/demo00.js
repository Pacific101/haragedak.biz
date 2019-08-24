

/**
 * Adds markers to the map highlighting the locations of the captials of
 * France, Italy, Germany, Spain and the United Kingdom.
 *
 * @param  {H.Map} map      A HERE Map instance within the application
 */
function addMarkersToMap(map,mylist) {
    var group = new H.map.Group();

    for (var i = 0; i < mylist.length; i++) {
      var myMarker = new H.map.Marker({lat:mylist[i],  lng:mylist[i+1]});
      map.addObject(myMarker);
      group.addObjects([myMarker]);
    }


    map.addObject(group);
    map.setViewBounds(group.getBounds());
  }


  /**
   * Boilerplate map initialization code starts below:
   */

  //Step 1: initialize communication with the platform
  // In your own code, replace variable app_id with your own app_id
  // and app_code with your own app_code
  var platform = new H.service.Platform({
    app_id: app_id,
    app_code: app_code,
    useCIT: true,
    useHTTPS: true
  });
  var defaultLayers = platform.createDefaultLayers();

  //Step 2: initialize a map - this map is centered over Europe
  var map = new H.Map(document.getElementById('map'),
    defaultLayers.normal.map,{
    center: {lat:50, lng:5},
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

  function obtain(callback,encoded) {
    $.ajax({
      url: location.protocol + `//geocoder.api.here.com/6.2/geocode.json?searchtext=${String(encoded)}&app_id=9i5wRuB2qSMk4QXNsHJF&app_code=jqCkp-06H39jgB7IuENe3Q&gen=9`,
      async: false,
      success: callback
    });
  }
  function myCallback(data) {
    mine.push(data.Response.View[0].Result[0].Location.DisplayPosition.Latitude);
    mine.push(data.Response.View[0].Result[0].Location.DisplayPosition.Longitude);
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
    addMarkersToMap(map,mine);

  });
