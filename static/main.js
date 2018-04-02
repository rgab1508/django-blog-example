// data-length="10"
// usrInput.attr('data-length', '12');
// usrInput.characterCounter();
$(document).ready(function(){
    $('#id_password1').attr('placeholder', 'Password');
    $('#id_password2').attr('placeholder', 'Confirm Password');
    $('#id_password').attr('placeholder', 'Password');
    $('#id_first_name').attr('placeholder', 'First Name ..');
    $('#id_last_name').attr('placeholder', 'Last Name ..');
    $('#id_email').attr('placeholder', 'Email ..')
    $('#id_bio').attr('placeholder', 'Bio ...')
    // pwd.attr('data-length', '15');
    // pwd.characterCounter();

    const cbody = $('#id_body');

    cbody.addClass('materialize-textarea');
    $(".button-collapse").sideNav();


    $('.tooltipped').tooltip({delay: 50});
});

// Getting a cookie by name
// using jQuery
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        let cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
let csrftoken = getCookie('csrftoken');

$(function () {
    $.ajaxSetup({
        headers: { "X-CSRFToken": getCookie("csrftoken") }
    });
});

/************  Media Query  *************/
// function myFunction(x) {
//     if (x.matches) { // If media query matches
//         document.body.style.backgroundColor = "yellow";
//     } else {
//         document.body.style.backgroundColor = "pink";
//     }
// }

// var x = window.matchMedia("(min-width: 700px)")
// myFunction(x) // Call listener function at run time
// x.addListener(myFunction) // Attach listener function on state changes