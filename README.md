# Map Views for CrossCompute

Render maps in your CrossCompute automations. Here are the views included in this package:

- map-mapbox
- map-deck-screengrid

Please see https://github.com/crosscompute/crosscompute for more information about the CrossCompute Analytics Automation Framework.

## Usage

```bash
# Upgrade package
pip install crosscompute-views-map --upgrade

# Update configuration
vim automate.yml
  variables:
    - id: buildings
      view: map-mapbox
    - id: incidents
      view: map-deck-screengrid
```
