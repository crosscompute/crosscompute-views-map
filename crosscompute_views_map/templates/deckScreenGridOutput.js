const {{ element_id }}_ = {
  data: '{{ data_uri }}',
  opacity: {{ opacity }},
  getPosition: d => d,
};
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
  layers: [
    new deck.ScreenGridLayer({{ element_id }}_),
  ],
{%- if for_print %}
  preserveDrawingBuffer: 1,
  glOptions: { preserveDrawingBuffer: 1 },
{%- endif %}
});
registerElement('{{ variable_id }}', function () {
  refreshMapDeckScreenGrid(
    '{{ element_id }}', '{{ data_uri }}', {{ element_id }}, {{ element_id }}_);
});
