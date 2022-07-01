function centerMarker(marker, map) {
  marker.setLngLat(map.getCenter());
  return marker;
}
const MAP_BY_ELEMENT_ID = {};
GET_DATA_BY_VIEW_NAME['$view_name'] = x => {
  const map = MAP_BY_ELEMENT_ID[x.id]
  const { _ne, _sw } = map.getBounds();
  const { lng, lat } = map.getCenter();
  const zoom = map.getZoom();
  return {
    value: {
      bounds: [_ne.lng, _ne.lat, _sw.lng, _sw.lat],
      center: [lng, lat],
      zoom,
    }
  };
};
