# TODO: Let creator override mapbox css and js
# TODO: Let creator override js template
import json
from os import environ

import geojson
import numpy as np
from crosscompute.routines.interface import Batch
from crosscompute.routines.variable import (
    Element, VariableView, add_label_html)

from ..constants import (
    DECK_JS_URI,
    MAPBOX_CSS_URI,
    MAPBOX_JS_URI,
    TURF_JS_URI)
from .asset import asset_storage


class MapMapboxView(VariableView):

    view_name = 'map-mapbox'
    environment_variable_definitions = [{'id': 'MAPBOX_TOKEN'}]
    css_uris = [MAPBOX_CSS_URI]
    js_uris = [MAPBOX_JS_URI, TURF_JS_URI]

    def process(self, path):
        with path.open('rt') as f:
            array = np.array(list(geojson.utils.coords(json.load(f))))
        save_map_configuration(array, path)

    def render_output(self, b: Batch, x: Element):
        variable_definition = self.variable_definition
        variable_id = self.variable_id
        element_id = x.id
        data_uri = b.get_data_uri(variable_definition, x)
        c = b.get_variable_configuration(variable_definition)
        main_text = get_map_html(
            element_id, variable_id, c, x.mode_name, self.view_name,
            x.design_name)
        js_texts = [
            "mapboxgl.accessToken = '%s';" % environ['MAPBOX_TOKEN'],
            MAP_MAPBOX_JS_HEADER,
            MAP_MAPBOX_OUTPUT_JS_HEADER,
            MAP_MAPBOX_OUTPUT_JS_VARIABLE.render({
                'variable_id': variable_id,
                'element_id': element_id,
                'data_uri': data_uri,
                'bounds': c.get('bounds'),
                'map': get_map_definition(element_id, c, x.for_print),
                'sources': get_source_definitions(element_id, c, data_uri),
                'layers': get_layer_definitions(element_id, c)})]
        return {
            'css_uris': self.css_uris, 'js_uris': self.js_uris,
            'main_text': main_text, 'js_texts': js_texts}


class MapMapboxLocationView(VariableView):

    view_name = 'map-mapbox-location'
    environment_variable_definitions = [{'id': 'MAPBOX_TOKEN'}]
    css_uris = [MAPBOX_CSS_URI]
    js_uris = [MAPBOX_JS_URI]

    def render_input(self, b: Batch, x: Element):
        variable_definition = self.variable_definition
        element_id = x.id
        view_name = self.view_name
        c = b.get_variable_configuration(variable_definition)
        data = b.load_data(variable_definition)
        if 'value' in data:
            v = data['value']
            try:
                longitude, latitude = v['center']
                zoom = v['zoom']
            except (KeyError, TypeError):
                longitude, latitude, zoom = 0, 0, 0
            c['longitude'], c['latitude'] = longitude, latitude
            c['zoom'] = zoom
        main_text = get_map_html(
            element_id, self.variable_id, c, x.mode_name, view_name,
            x.design_name, MAP_MAPBOX_LOCATION_INPUT_HTML.render({
                'view_name': view_name, 'element_id': element_id}))
        js_texts = [
            "mapboxgl.accessToken = '%s';" % environ['MAPBOX_TOKEN'],
            MAP_MAPBOX_JS_HEADER,
            MAP_MAPBOX_LOCATION_INPUT_JS_HEADER.render({
                'view_name': view_name}),
            MAP_MAPBOX_LOCATION_INPUT_JS_VARIABLE.render({
                'element_id': element_id,
                'map': get_map_definition(element_id, c, x.for_print)}),
        ]
        return {
            'css_uris': self.css_uris, 'js_uris': self.js_uris,
            'main_text': main_text, 'js_texts': js_texts}


class MapDeckScreenGridView(VariableView):

    view_name = 'map-deck-screengrid'
    environment_variable_definitions = [{'id': 'MAPBOX_TOKEN'}]
    css_uris = [MAPBOX_CSS_URI]
    js_uris = [MAPBOX_JS_URI, DECK_JS_URI]

    def process(self, path):
        with path.open('rt') as f:
            array = np.array(json.load(f))
        save_map_configuration(array, path)

    def render_output(self, b: Batch, x: Element):
        variable_definition = self.variable_definition
        variable_id = self.variable_id
        element_id = x.id
        data_uri = b.get_data_uri(variable_definition, x)
        c = b.get_variable_configuration(variable_definition)
        mapbox_token = environ['MAPBOX_TOKEN']
        main_text = get_map_html(
            element_id, variable_id, c, x.mode_name, self.view_name,
            x.design_name)
        js_texts = [
            f"mapboxgl.accessToken = '{mapbox_token}';",
            MAP_DECK_SCREENGRID_OUTPUT_JS_HEADER,
            MAP_DECK_SCREENGRID_OUTPUT_JS_VARIABLE.render({
                'variable_id': variable_id,
                'element_id': element_id,
                'data_uri': data_uri,
                'opacity': c.get('opacity', 0.5),
                'get_position_definition_string': c.get('position', 'd => d'),
                'get_weight_definition_string': c.get('weight', 1),
                'style_uri': c.get('style', MAP_MAPBOX_STYLE_URI),
                'bounds': c.get('bounds'),
                'longitude': c.get('longitude', 0),
                'latitude': c.get('latitude', 0),
                'zoom': c.get('zoom', 0),
                'for_print': x.for_print})]
        return {
            'css_uris': self.css_uris, 'js_uris': self.js_uris,
            'main_text': main_text, 'js_texts': js_texts}


def save_map_configuration(xy_array, source_path):
    try:
        xs = xy_array[:, 0]
        ys = xy_array[:, 1]
    except IndexError:
        d = {
            'longitude': 0,
            'latitude': 0,
            'zoom': 0,
        }
    else:
        d = {
            'longitude': xs.mean(),
            'latitude': ys.mean(),
        }
        if len(xs) == 1:
            d['zoom'] = 15
        else:
            d['bounds'] = xs.min(), ys.min(), xs.max(), ys.max()
    with open(str(source_path) + '.configuration', 'wt') as f:
        json.dump(d, f)


def get_map_html(
        element_id, variable_id, variable_configuration, mode_name, view_name,
        design_name, prefix_html=''):
    main_text = prefix_html + MAP_MAPBOX_HTML.substitute({
        'element_id': element_id,
        'mode_name': mode_name,
        'view_name': view_name,
        'variable_id': variable_id,
    })
    if design_name not in ['none']:
        main_text = add_label_html(
            main_text, variable_configuration, variable_id, element_id)
    return main_text


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
            d['id'] = element_id
        if 'source' not in d:
            d['source'] = element_id
        definitions.append(d)
    return definitions


MAP_MAPBOX_STYLE_URI = 'mapbox://styles/mapbox/dark-v10'


MAP_MAPBOX_HTML = asset_storage.load_string_text('mapbox.html')
MAP_MAPBOX_JS_HEADER = asset_storage.load_raw_text('mapbox-header.js')
MAP_MAPBOX_OUTPUT_JS_HEADER = asset_storage.load_raw_text(
    'mapbox-output-header.js')
MAP_MAPBOX_OUTPUT_JS_VARIABLE = asset_storage.load_jinja_text(
    'mapbox-output-variable.js')


MAP_MAPBOX_LOCATION_INPUT_HTML = asset_storage.load_jinja_text(
    'mapbox-location-input.html')
MAP_MAPBOX_LOCATION_INPUT_JS_HEADER = asset_storage.load_jinja_text(
    'mapbox-location-input-header.js')
MAP_MAPBOX_LOCATION_INPUT_JS_VARIABLE = asset_storage.load_jinja_text(
    'mapbox-location-input-variable.js')


MAP_DECK_SCREENGRID_OUTPUT_JS_HEADER = asset_storage.load_raw_text(
    'deck-screengrid-output-header.js')
MAP_DECK_SCREENGRID_OUTPUT_JS_VARIABLE = asset_storage.load_jinja_text(
    'deck-screengrid-output-variable.js')
