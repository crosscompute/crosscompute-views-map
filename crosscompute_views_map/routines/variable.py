# TODO: Let creator override mapbox css and js
# TODO: Let creator override js template
from crosscompute.routines.interface import Batch
from crosscompute.routines.variable import Element, VariableView
from jinja2 import Template
from os import environ

from ..constants import (
    DECK_JS_URI,
    MAPBOX_CSS_URI,
    MAPBOX_JS_URI,
    TEMPLATES_FOLDER)


class MapMapboxView(VariableView):

    view_name = 'map-mapbox'
    environment_variable_definitions = [{'id': 'MAPBOX_TOKEN'}]
    css_uris = [MAPBOX_CSS_URI]
    js_uris = [MAPBOX_JS_URI]

    def render_output(self, b: Batch, x: Element):
        variable_definition = self.variable_definition
        variable_id = self.variable_id
        element_id = x.id
        data_uri = b.get_data_uri(variable_definition, x)
        c = b.get_variable_configuration(variable_definition)
        body_text = (
            f'<div id="{element_id}" '
            f'class="{self.mode_name} {self.view_name} {variable_id}"></div>')
        mapbox_token = environ['MAPBOX_TOKEN']
        js_texts = [
            f"mapboxgl.accessToken = '{mapbox_token}';",
            MAP_MAPBOX_HEADER,
            MAP_MAPBOX_OUTPUT.render({
                'variable_id': variable_id,
                'element_id': element_id,
                'data_uri': data_uri,
                'map': get_map_definition(element_id, c, x.for_print),
                'sources': get_source_definitions(element_id, c, data_uri),
                'layers': get_layer_definitions(element_id, c),
            }),
        ]
        return {
            'css_uris': self.css_uris,
            'js_uris': self.js_uris,
            'body_text': body_text,
            'js_texts': js_texts,
        }


class MapDeckScreenGridView(VariableView):

    view_name = 'map-deck-screengrid'
    environment_variable_definitions = [{'id': 'MAPBOX_TOKEN'}]
    css_uris = [MAPBOX_CSS_URI]
    js_uris = [MAPBOX_JS_URI, DECK_JS_URI]

    def render_output(self, b: Batch, x: Element):
        variable_definition = self.variable_definition
        variable_id = self.variable_id
        element_id = x.id
        data_uri = b.get_data_uri(variable_definition, x)
        c = b.get_variable_configuration(variable_definition)
        body_text = (
            f'<div id="{element_id}" '
            f'class="{self.mode_name} {self.view_name} {variable_id}"></div>')
        mapbox_token = environ['MAPBOX_TOKEN']
        js_texts = [
            f"mapboxgl.accessToken = '{mapbox_token}';",
            MAP_DECK_SCREENGRID_HEADER,
            MAP_DECK_SCREENGRID_OUTPUT.render({
                'variable_id': variable_id,
                'element_id': element_id,
                'data_uri': data_uri,
                'opacity': c.get('opacity', 0.5),
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


def load_view_text(file_name):
    return open(TEMPLATES_FOLDER / file_name).read().strip()


MAP_MAPBOX_STYLE_URI = 'mapbox://styles/mapbox/dark-v10'


MAP_MAPBOX_HEADER = load_view_text('mapboxHeader.js')
MAP_MAPBOX_OUTPUT = Template(load_view_text('mapboxOutput.js'))


MAP_DECK_SCREENGRID_HEADER = load_view_text(
    'deckScreenGridHeader.js')
MAP_DECK_SCREENGRID_OUTPUT = Template(load_view_text(
    'deckScreenGridOutput.js'))
