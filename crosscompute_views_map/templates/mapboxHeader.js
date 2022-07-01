const mapboxGeolocateControl = new mapboxgl.GeolocateControl({
  positionOptions: { enableHighAccuracy: true },
  showAccuracyCircle: true,
  showUserHeading: true,
  trackUserLocation: true
});
const mapboxFullscreenControl = new mapboxgl.FullscreenControl();
