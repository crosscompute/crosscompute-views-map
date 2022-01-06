# Map Views for CrossCompute

Render maps in your CrossCompute automations.

- map-mapbox
- map-pydeck-screengrid

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
      view: map-pydeck-screengrid
```
