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