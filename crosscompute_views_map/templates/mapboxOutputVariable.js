const {{ element_id }} = new mapboxgl.Map({{ map }})
  .addControl(new mapboxgl.GeolocateControl({
    positionOptions: { enableHighAccuracy: true },
    showAccuracyCircle: true,
    showUserHeading: true,
    trackUserLocation: true
  }))
  .addControl(new mapboxgl.FullscreenControl());
{{ element_id }}.on('load', () => {
const m = {{ element_id }};
{% for source in sources %}
  m.addSource('{{ source.pop('id') }}', {{ source }});
{% endfor %}
{% for layer in layers %}
  m.addLayer({{ layer }});
{% endfor %}
{% if bounds %}
  jumpToBounds(m, {{ bounds }});
{% endif %}
});
registerElement('{{ variable_id }}', function () {
  refreshMapMapbox('{{ element_id }}', '{{ data_uri }}', {{ element_id }});
});
