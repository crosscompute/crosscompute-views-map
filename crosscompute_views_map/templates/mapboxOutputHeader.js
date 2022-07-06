function refreshMapMapbox(elementId, dataUri, mapInstance) {
  mapInstance.jumpTo({
    longitude: 0,
    latitude: 0,
    zoom: 0,
  }).once('sourcedata', function() {
    const features = mapInstance.querySourceFeatures(elementId);
    if (!features.length) return;
    const bounds = turf.bbox(turf.featureCollection(features));
    jumpToBounds(mapInstance, bounds);
  }).getSource(elementId).setData(dataUri + '?' + Date.now());
}
function jumpToBounds(mapInstance, bounds) {
  mapInstance.jumpTo(mapInstance.cameraForBounds(bounds));
}
