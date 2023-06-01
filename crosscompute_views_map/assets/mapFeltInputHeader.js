// GET_DATA_BY_VIEW_NAME['$view_name'] = async? x => {
GET_DATA_BY_VIEW_NAME['$view_name'] = x => {
  const map = x.querySelector('#felt_url').value;
  try {
    let feltUrl = new URL(map);
    if (feltUrl.hostname !== 'felt.com') return;
    let geojsonUrl = 'https://' + feltUrl.hostname + '/' + feltUrl.pathname + '.geojson'
    /*
      fetch(geojsonUrl)
        .then(response => response.body)
        .then(body => body.toJSON())
        .then(geojson => feltGeojson.value = geojson)
        .catch(e => {
          console.log(e);

        })
    */
    console.log(geojsonUrl)
    return {
      uri: geojsonUrl
    }
  } catch (e) {
    console.log(e)
  }
  return ''
};

function isFeltURL(url) {
  try {
    let feltUrl = new URL(url);
    if (feltUrl.hostname === 'felt.com') return true;
  } catch (e) {}
  return false;
}

function getFeltPath(url) {
  try {
    let feltUrl = new URL(url);
    if (feltUrl.hostname === 'felt.com') return feltUrl.pathname;
  } catch (e) {}
  return false;
}

async function refreshFelt(elementId, elementAttribute, dataUri, dataValue) {
  let x = dataValue;
  if (x === undefined) {
    try {
      const r = await fetch(dataUri), { status } = r;
      if (status != 200) return;
      x = await r.text();
    } catch {
      return;
    }
  }

  // Refresh felt embed preview
  //  document.getElementById(elementId).contentWindow.location.reload();

  const l = document.getElementById(elementId);
  l[elementAttribute] = typeof x === 'object' ? JSON.stringify(x) : x;
  return l;
}
