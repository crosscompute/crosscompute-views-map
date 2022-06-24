const {{ element_id }} = new mapboxgl.Map({{ map }});
{{ element_id }}.on('load', () => {
{%- for source in sources %}
  {{ element_id }}.addSource('{{ source.pop('id') }}', {{ source }});
{%- endfor %}
{%- for layer in layers %}
  {{ element_id }}.addLayer({{ layer }});
{%- endfor %}
});
registerElement('{{ variable_id }}', function () {
  refreshMapMapbox('{{ element_id }}', '{{ data_uri }}', {{ element_id }});
});
