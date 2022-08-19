function refreshMapMapbox(elementId, dataUri, map) {
  map.getSource(elementId).setData(dataUri + '?' + Date.now());
}
function jumpToBounds(map, bounds) {
  map.jumpTo(map.cameraForBounds(bounds));
}
