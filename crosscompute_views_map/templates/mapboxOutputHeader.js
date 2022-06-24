function refreshMapMapbox(elementId, dataUri, mapInstance) {
  mapInstance.getSource(elementId).setData(dataUri + '?' + Date.now());
}
