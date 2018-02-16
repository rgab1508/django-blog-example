const usrInput = $('#id_username');
usrInput.attr('placeholder', 'Username');
// data-length="10"
// usrInput.attr('data-length', '12');
// usrInput.characterCounter();
const pwdInput = $('#id_password1');
pwdInput.attr('placeholder', 'Password');
const cfmPwd = $('#id_password2');
cfmPwd.attr('placeholder', 'Confirm Password');
const pwd = $('#id_password');
pwd.attr('placeholder', 'Password');
// pwd.attr('data-length', '15');
// pwd.characterCounter();

const cbody = $('#id_body');

cbody.addClass('materialize-textarea');
$(".button-collapse").sideNav();
