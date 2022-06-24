const {{ element_id }} = new mapboxgl.Map({{ map }})
  .addControl(new mapboxgl.GeolocateControl({
    positionOptions: { enableHighAccuracy: true },
    showAccuracyCircle: true,
    showUserHeading: true,
    trackUserLocation: true
  }));
const {{ element_id }}_marker = centerMarker(new mapboxgl.Marker(), {{ element_id }}).addTo({{ element_id }});
{{ element_id }}.on('move', () => {
  centerMarker({{ element_id }}_marker, {{ element_id }});
});
MAP_BY_ELEMENT_ID['{{ element_id }}'] = {{ element_id }};
