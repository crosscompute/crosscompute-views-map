const {{ element_id }} = setupMapMapbox(new mapboxgl.Map({{ map }}), '{{ element_id }}');
{{ element_id }}.on('load', () => {
const m = {{ element_id }};
{% for source in sources %}
  m.addSource('{{ source.pop('id') }}', {{ source }});
{% endfor %}
{% for layer in layers %}
  m.addLayer({{ layer }});
{% endfor %}
{% if bounds %}
  jumpToBounds(m, {{ bounds }});
{% endif %}
});
registerElement('{{ variable_id }}', function () {
  refreshMapMapbox('{{ element_id }}', '{{ data_uri }}', {{ element_id }});
});
