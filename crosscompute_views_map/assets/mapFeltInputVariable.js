(async function () {
  const l = await refreshFelt('{{element_id}}', 'value', '{{data_uri}}');
  if (l) {
    l.disabled = false;
  }
  let element = document.querySelector('#{{element_id}}');
  let input = element.querySelector("input");
  input.addEventListener('change', e => {
    let value = e.target.value;
    let iframe = element.querySelector("iframe");
    if (isFeltURL(value)) {
      let path = getFeltPath(value);
      iframe.src = `https://felt.com/embed${path}`;
      iframe.style.display = 'block'
    } else {
      iframe.style.display = 'none'
    }
  })


})();

