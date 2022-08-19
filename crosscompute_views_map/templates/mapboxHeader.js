function setupMapMapbox(map, elementId) {
  const geolocateControl = new mapboxgl.GeolocateControl({
    positionOptions: { enableHighAccuracy: true },
    showAccuracyCircle: true,
    showUserHeading: true,
    trackUserLocation: true,
  });
  const fullscreenControl = new mapboxgl.FullscreenControl();
  const navigationControl = new mapboxgl.NavigationControl({
    visualizePitch: true,
  });
  const scaleControl = new mapboxgl.ScaleControl();
  map.controlByName = {
    geolocate: geolocateControl,
    fullscreen: fullscreenControl,
    navigation: navigationControl,
    scale: scaleControl,
  };
  return map
    .once('sourcedata', function(e) {
      if (!e.isSourceLoaded) return;
      const features = map.querySourceFeatures(elementId);
      if (!features.length) return;
      const bounds = turf.bbox(turf.featureCollection(features));
      jumpToBounds(map, bounds);
    })
    .addControl(geolocateControl)
    .addControl(fullscreenControl, 'bottom-right')
    .addControl(navigationControl, 'top-left')
    .addControl(scaleControl, 'bottom-left');
}
