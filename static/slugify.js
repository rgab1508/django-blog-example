const _title = document.querySelector(input[name=title]);

const _slug = document.querySelector(input[name=slug]);

const slugify = (v) => {
    return v.toString().toLowerCase().trim()
        .replace(/&/g, '-and-')
        .replace(/[\s\W-]+/g, '-')
};

_title.addEventListner('keyup', (e) =>{
    _slug.setAttribute('value', slugify(_title.value));
});