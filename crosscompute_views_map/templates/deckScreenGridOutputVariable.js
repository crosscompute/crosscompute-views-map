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
{% if for_print %}
  preserveDrawingBuffer: 1,
  glOptions: { preserveDrawingBuffer: 1 },
{% endif %}
});
{% if bounds != 'null' %}
(function () {
  const { center, zoom } = {{ element_id }}.getMapboxMap().cameraForBounds({{ bounds }});

})();
const viewState = { longitude: camera.center.lng, latitude: camera.center.lat, zoom: Math.trunc(camera.zoom) };
{{ element_id }}.setProps({
  viewState: viewState,
});
{% endif %}
registerElement('{{ variable_id }}', function () {
  refreshMapDeckScreenGrid(
    '{{ element_id }}', '{{ data_uri }}', {{ element_id }}, {{ element_id }}_);
});
