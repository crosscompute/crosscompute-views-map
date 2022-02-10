# TODO: Detect from url parameters whether we are rendering a pdf
# TODO: Let creator override mapbox css and js
# TODO: Let creator override js template
from crosscompute.macros.configuration import get_environment_value
from crosscompute.routines.variable import VariableElement, VariableView
from jinja2 import Template


class MapMapboxView(VariableView):

    view_name = 'map-mapbox'
    css_uris = [
        'https://api.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.css',
    ]
    js_uris = [
        'https://api.mapbox.com/mapbox-gl-js/v2.6.1/mapbox-gl.js',
    ]

    def render_output(self, x: VariableElement):
        element_id = x.id
        variable_id = self.variable_id
        body_text = (
            f'<div id="{element_id}" '
            f'class="{self.view_name} {variable_id}"></div>')
        mapbox_token = get_environment_value('MAPBOX_TOKEN', '')
        c = self.configuration
        js_texts = [
            f"mapboxgl.accessToken = '{mapbox_token}';",
            MAP_MAPBOX_JS_TEMPLATE.render({
                'element_id': element_id,
                'map': get_map_definition(element_id, c, x.for_print),
                'sources': get_source_definitions(element_id, c, x.uri),
                'layers': get_layer_definitions(element_id, c),
            }),
        ]
        return {
            'css_uris': self.css_uris,
            'js_uris': self.js_uris,
            'body_text': body_text,
            'js_texts': js_texts,
        }


def get_map_definition(element_id, variable_configuration, for_print):
    style_uri = variable_configuration.get('style', MAP_MAPBOX_STYLE_URI)
    longitude = variable_configuration.get('longitude', 0)
    latitude = variable_configuration.get('latitude', 0)
    zoom = variable_configuration.get('zoom', 0)
    d = {
        'container': element_id,
        'style': style_uri,
        'center': [longitude, latitude],
        'zoom': zoom,
    }
    if for_print:
        d['preserveDrawingBuffer'] = 1
    return d


def get_source_definitions(element_id, variable_configuration, data_uri):
    return variable_configuration.get('sources', [{
        'id': element_id,
        'type': 'geojson',
        'data': data_uri,
    }])


def get_layer_definitions(element_id, variable_configuration):
    definitions = []
    for index, d in enumerate(variable_configuration.get('layers', [{
        'type': 'circle',
    }])):
        if 'id' not in d:
            d['id'] = f'l{index}'
        if 'source' not in d:
            d['source'] = element_id
        definitions.append(d)
    return definitions


MAP_MAPBOX_JS_TEMPLATE = Template('''\
const {{ element_id }} = new mapboxgl.Map({{ map }});
{{ element_id }}.on('load', () => {
{%- for source in sources %}
  {{ element_id }}.addSource('{{ source.pop('id') }}', {{ source }});
{%- endfor %}
{%- for layer in layers %}
  {{ element_id }}.addLayer({{ layer }});
{%- endfor %}
});''')
MAP_MAPBOX_STYLE_URI = 'mapbox://styles/mapbox/dark-v10'
