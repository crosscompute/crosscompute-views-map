const {{ element_id }}LayerOptions = {
  data: '{{ data_uri }}',
  opacity: {{ opacity }},
  getPosition: d => d,
};
const {{ element_id }}Layer = new deck.ScreenGridLayer({{ element_id }}LayerOptions);
const {{ element_id }} = new deck.DeckGL({
  container: '{{ element_id }}',
  mapboxApiAccessToken: mapboxgl.accessToken,
  mapStyle: '{{ style_uri }}',
  initialViewState: {
    longitude: {{ longitude }},
    latitude: {{ latitude }},
    zoom: {{ zoom }},
  },
  controller: true,
  layers: [ {{ element_id }}Layer ],
{% if for_print %}
  preserveDrawingBuffer: 1,
  glOptions: { preserveDrawingBuffer: 1 },
{% endif %}
});
{% if bounds or not zoom %}
const {{ element_id }}UpdateViewStateIntervalId = setInterval(function() {
  console.log('hey');
{% if bounds %}
  const bounds = {{ bounds }};
{% else %}
  const bounds = {{ element_id }}Layer.getBounds();
{% endif %}
  if (!bounds) return;
  clearInterval({{ element_id }}UpdateViewStateIntervalId);
  const { center, zoom } = {{ element_id }}.getMapboxMap().cameraForBounds(bounds);
  {{ element_id }}.setProps({
    initialViewState: { longitude: center.lng, latitude: center.lat, zoom: Math.trunc(zoom) },
  });
}, 100);
{% endif %}
registerElement('{{ variable_id }}', function () {
  refreshMapDeckScreenGrid('{{ element_id }}', '{{ data_uri }}', {{ element_id }}, {{ element_id }}LayerOptions);
});
