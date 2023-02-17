async function refreshMapDeckScreenGrid(elementId, dataUri, deckInstance, layerOptions) {
  layerOptions.data = dataUri + '?' + Date.now();
  deckInstance.setProps({ layers: [new deck.ScreenGridLayer(layerOptions)] });
}
