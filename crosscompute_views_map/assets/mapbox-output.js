const {{ element_id }} = setupMapMapbox(new mapboxgl.Map({{ map }}), '{{ element_id }}');
{{ element_id }}.on('load', () => {
{% for source in sources %}
  {{ element_id }}.addSource('{{ source.pop('id') }}', {{ source }});
{% endfor %}
{% for layer in layers %}
  {{ element_id }}.addLayer({{ layer }});
{% endfor %}
{% if bounds %}
  jumpToBounds({{ element_id }}, {{ bounds }});
{% endif %}
});
registerFunction('{{ variable_id }}', async function() {
  while (!{{ element_id }}.loaded()) {
    await sleep(1000);
  }
  await refreshMapMapbox('{{ element_id }}', '{{ data_uri }}', {{ element_id }});
});
