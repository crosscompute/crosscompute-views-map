function addMapboxControls(map) {
  return map
    .addControl(new mapboxgl.GeolocateControl({
      positionOptions: { enableHighAccuracy: true },
      showAccuracyCircle: true,
      showUserHeading: true,
      trackUserLocation: true
    }))
    .addControl(new mapboxgl.FullscreenControl({
    }), 'bottom-right')
    .addControl(new mapboxgl.NavigationControl({
      visualizePitch: true,
    }), 'top-left')
    .addControl(new mapboxgl.ScaleControl({
    }), 'bottom-left');
}
