const {{ element_id }} = setupMapMapbox(new mapboxgl.Map({{ map }}), '{{ element_id }}');
const {{ element_id }}_marker = centerMarker(new mapboxgl.Marker(), {{ element_id }}).addTo({{ element_id }});
{{ element_id }}.on('move', function() {
  centerMarker({{ element_id }}_marker, {{ element_id }});
});
MAP_BY_ELEMENT_ID['{{ element_id }}'] = {{ element_id }};
