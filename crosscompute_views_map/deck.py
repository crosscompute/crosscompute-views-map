from crosscompute.macros.configuration import get_environment_value
from crosscompute.routines.interface import BatchInterface
from crosscompute.routines.variable import Element, VariableView
from jinja2 import Template

from .mapbox import MAP_MAPBOX_STYLE_URI


class MapDeckScreenGridView(VariableView):

    view_name = 'map-deck-screengrid'
    css_uris = [
        'https://api.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.css',
    ]
    js_uris = [
        'https://unpkg.com/deck.gl@^8.0.0/dist.min.js',
        'https://api.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.js',
    ]

    def render_output(self, b: BatchInterface, x: Element):
        variable_definition = self.variable_definition
        data_uri = b.get_data_uri(variable_definition)
        c = b.get_variable_configuration(variable_definition)
        element_id = x.id
        variable_id = self.variable_id
        body_text = (
            f'<div id="{element_id}" '
            f'class="{self.mode_name} {self.view_name} {variable_id}"></div>')
        mapbox_token = get_environment_value('MAPBOX_TOKEN', '')
        js_texts = [
            f"mapboxgl.accessToken = '{mapbox_token}';",
            MAP_DECK_SCREENGRID_JS_TEMPLATE.render({
                'data_uri': data_uri,
                'opacity': c.get('opacity', 0.5),
                'element_id': element_id,
                'style_uri': c.get('style', MAP_MAPBOX_STYLE_URI),
                'longitude': c.get('longitude', 0),
                'latitude': c.get('latitude', 0),
                'zoom': c.get('zoom', 0),
                'for_print': x.for_print,
            }),
        ]
        return {
            'css_uris': self.css_uris,
            'js_uris': self.js_uris,
            'body_text': body_text,
            'js_texts': js_texts,
        }


MAP_DECK_SCREENGRID_JS_TEMPLATE = Template('''\
new deck.DeckGL({
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
    new deck.ScreenGridLayer({
        data: '{{ data_uri }}',
        getPosition: d => d,
        opacity: {{ opacity }},
    }),
  ],
{%- if for_print %}
  preserveDrawingBuffer: 1,
  glOptions: { preserveDrawingBuffer: 1 },
{%- endif %}
});''')
