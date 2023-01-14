import json
from os import getenv
from pathlib import Path
from random import uniform
from time import sleep


def get_random_coordinates():
    longitude = uniform(-180, 180)
    latitude = uniform(-90, 90)
    return longitude, latitude


input_folder = Path(getenv(
    'CROSSCOMPUTE_INPUT_FOLDER', 'batches/standard/input'))
output_folder = Path(getenv(
    'CROSSCOMPUTE_OUTPUT_FOLDER', 'batches/standard/output'))
output_folder.mkdir(exist_ok=True)


with (input_folder / 'variables.dictionary').open('rt') as f:
    d = json.load(f)


sleep(d['delay_in_seconds'])


with (output_folder / 'features.geojson').open('wt') as f:
    json.dump({
        'type': 'FeatureCollection',
        'features': [{
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': get_random_coordinates(),
            },
        }, {
            'type': 'Feature',
            'geometry': {
                'type': 'Point',
                'coordinates': get_random_coordinates(),
            },
        }],
    }, f)
