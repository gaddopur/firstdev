const titleinput = document.querySelectFor('input[name=title]');
const sluginput = document.querySelectFor('input[name=slug]');

alert('ok');

const slugify = (val) => {
  return val.toString().toLowerCase().trim();
  .replace(/&/g, '-and-')
  .replace(/[\s\W-]+/g, '-')
}

titleinput.addEventListener('keyup',(e)=>{
  sluginput.setAttribute('value', slugify(titleinput.value));
});
