# TODO: Let creator override mapbox css and js
from crosscompute.macros.configuration import get_environment_value
from crosscompute.routines.variable import VariableView
from string import Template


class MapMapboxView(VariableView):

    view_name = 'map-mapbox'
    is_asynchronous = True
    css_uris = [
        'https://api.mapbox.com/mapbox-gl-js/v2.6.0/mapbox-gl.css',
    ]
    js_uris = [
        'https://api.mapbox.com/mapbox-gl-js/v2.6.0/mapbox-gl.js',
    ]

    def render_output(self, element_id, function_names, request_path):
        variable_id = self.variable_id
        body_text = (
            f'<div id="{element_id}" '
            f'class="{self.view_name} {variable_id}"></div>')
        mapbox_token = get_environment_value('MAPBOX_TOKEN', '')
        variable_configuration = self.configuration
        js_texts = [
            f"mapboxgl.accessToken = '{mapbox_token}'",
            MAP_MAPBOX_JS_TEMPLATE.substitute({
                'element_id': element_id,
                'data_uri': request_path + '/' + variable_id,
                'style_uri': variable_configuration.get(
                    'style', MAP_MAPBOX_STYLE_URI),
                'longitude': variable_configuration.get('longitude', 0),
                'latitude': variable_configuration.get('latitude', 0),
                'zoom': variable_configuration.get('zoom', 0),
            }),
        ]
        # TODO: Allow specification of preserveDrawingBuffer
        return {
            'css_uris': self.css_uris,
            'js_uris': self.js_uris,
            'body_text': body_text,
            'js_texts': js_texts,
        }


MAP_MAPBOX_JS_TEMPLATE = Template('''\
const $element_id = new mapboxgl.Map({
  container: '$element_id',
  style: '$style_uri',
  center: [$longitude, $latitude],
  zoom: $zoom,
  // preserveDrawingBuffer: true,
});
$element_id.on('load', () => {
  $element_id.addSource('$element_id', {
    type: 'geojson',
    data: '$data_uri'})
  $element_id.addLayer({
    id: '$element_id',
    type: 'fill',
    source: '$element_id'})
});''')
MAP_MAPBOX_STYLE_URI = 'mapbox://styles/mapbox/dark-v10'
