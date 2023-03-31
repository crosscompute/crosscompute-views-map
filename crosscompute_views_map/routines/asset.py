from crosscompute.routines.asset import AssetStorage

from ..constants import ASSETS_FOLDER


asset_storage = AssetStorage(ASSETS_FOLDER)


MAP_CSS = asset_storage.load_raw_text('map.css')


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
