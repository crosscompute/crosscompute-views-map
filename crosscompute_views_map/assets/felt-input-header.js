/*
GET_DATA_BY_VIEW_NAME['$view_name'] = x => {
  const map = x.querySelector('#felt_url').value;
  try {
    let feltUrl = new URL(map);
    if (feltUrl.hostname !== 'felt.com') return;
    let geojsonUrl = 'https://' + feltUrl.hostname + '/' + feltUrl.pathname + '.geojson'
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

async function refreshFelt(elementId, dataUri) {
  try {
    const r = await fetch(dataUri), { status } = r;
    if (status != 200) return;
    x = await r.text();
  } catch {
    return;
  }
  const l = document.getElementById(elementId);
  l.value = typeof x === 'object' ? JSON.stringify(x) : x;
  return l;
}
*/
