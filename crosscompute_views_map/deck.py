from crosscompute.macros.configuration import get_environment_value
from crosscompute.routines.variable import VariableView
from string import Template

from .mapbox import MAP_MAPBOX_STYLE_URI


class MapDeckScreenGridView(VariableView):

    view_name = 'map-deck-screengrid'
    is_asynchronous = True
    css_uris = [
        'https://api.mapbox.com/mapbox-gl-js/v2.6.0/mapbox-gl.css',
    ]
    js_uris = [
        'https://unpkg.com/deck.gl@^8.0.0/dist.min.js',
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
            MAP_PYDECK_SCREENGRID_JS_TEMPLATE.substitute({
                'data_uri': request_path + '/' + variable_id,
                'opacity': variable_configuration.get('opacity', 0.5),
                'element_id': element_id,
                'mapbox_token': mapbox_token,
                'style_uri': variable_configuration.get(
                    'style', MAP_MAPBOX_STYLE_URI),
                'longitude': variable_configuration.get('longitude', 0),
                'latitude': variable_configuration.get('latitude', 0),
                'zoom': variable_configuration.get('zoom', 0),
            }),
        ]
        return {
            'css_uris': self.css_uris,
            'js_uris': self.js_uris,
            'body_text': body_text,
            'js_texts': js_texts,
        }


MAP_PYDECK_SCREENGRID_JS_TEMPLATE = Template('''\
const layers = [
  new deck.ScreenGridLayer({
    data: '$data_uri',
    getPosition: d => d,
    opacity: $opacity,
  }),
];
new deck.DeckGL({
  container: '$element_id',
  mapboxApiAccessToken: '$mapbox_token',
  mapStyle: '$style_uri',
  initialViewState: {
    longitude: $longitude,
    latitude: $latitude,
    zoom: $zoom,
  },
  controller: true,
  layers,
  /*
  preserveDrawingBuffer: true,
  glOptions: {
    preserveDrawingBuffer: true,
  },
  */
});
''')
