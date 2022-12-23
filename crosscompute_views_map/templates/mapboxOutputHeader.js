async function refreshMapMapbox(elementId, dataUri, map) {
  const r = await fetch(dataUri), { status } = r;
  if (status != 200) {
    throw { status };
  }
  const d = await r.json(), bounds = turf.bbox(d);
  map.getSource(elementId).setData(d);
  jumpToBounds(map, bounds);
}
function jumpToBounds(map, bounds) {
  map.jumpTo(map.cameraForBounds(bounds));
}
