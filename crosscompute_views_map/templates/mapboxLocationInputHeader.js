function centerMarker(marker, map) {
  marker.setLngLat(map.getCenter());
  return marker;
}
MAP_BY_ELEMENT_ID = {};
GET_DATA_BY_VIEW_NAME['$view_name'] = x => {
  const center = MAP_BY_ELEMENT_ID[x.id].getCenter();
  return { value: [center.lng, center.lat] };
};
