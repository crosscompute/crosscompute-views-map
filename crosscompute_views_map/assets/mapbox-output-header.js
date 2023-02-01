async function refreshMapMapbox(elementId, dataUri, map) {
  let d;
  try {
    const r = await fetch(dataUri);
    d = await r.json();
  } catch {
    return;
  }
  map.getSource(elementId).setData(d);
  jumpToBounds(map, turf.bbox(d));
}
function jumpToBounds(map, bounds) {
  map.jumpTo(map.cameraForBounds(bounds));
}
