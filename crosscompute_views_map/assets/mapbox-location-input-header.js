function centerMarker(marker, map) {
  marker.setLngLat(map.getCenter());
  return marker;
}
const MAP_BY_ELEMENT_ID = {};
GET_DATA_BY_VIEW_NAME['{{ view_name }}'] = x => {
  const map = MAP_BY_ELEMENT_ID[x.id], { _ne, _sw } = map.getBounds(), { lng, lat } = map.getCenter(), zoom = map.getZoom();
  return {
    value: { bounds: [_sw.lng, _sw.lat, _ne.lng, _ne.lat], center: [lng, lat], zoom },
  };
};
for (var l of document.getElementsByClassName('_{{ view_name }}-geolocate')) {
  if (isSecure) {
    l.onclick = function() {
      const { element: elementId } = l.dataset;
      MAP_BY_ELEMENT_ID[elementId].controlByName.geolocate.trigger();
    }
  } else {
    l.disabled = true;
    l.innerHTML = 'Geolocation is disabled because connection is not secure';
  }
}
