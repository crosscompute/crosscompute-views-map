# Map Views for CrossCompute

Render maps in your CrossCompute automations. Here are the views included in this package:

- map-mapbox
- map-mapbox-location
- map-deck-screengrid

Please see https://github.com/crosscompute/crosscompute for more information about the CrossCompute Analytics Automation Framework.

## Usage

```bash
# Upgrade package
pip install crosscompute-views-map

# Update configuration
vim automate.yml
  input:
    variables:
      - id: incident
        view: map-mapbox-location
  output:
    variables:
      - id: buildings
        view: map-mapbox
      - id: incidents
        view: map-deck-screengrid
```

## Troubleshooting

### No Matching Distribution Found

```
$ pip install crosscompute-views-map
ERROR: Could not find a version that satisfies the requirement crosscompute-views-map (from versions: none)
ERROR: No matching distribution found for crosscompute-views-map
```

To solve this issue, create a virtual environment using python >= 3.9.

```
sudo dnf -y install python3.9
# sudo apt -y install python3.9
python3.9 -m venv ~/.virtualenvs/crosscompute
source ~/.virtualenvs/crosscompute/bin/activate
pip install crosscompute-views-map
```
