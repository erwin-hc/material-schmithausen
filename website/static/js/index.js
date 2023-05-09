// ---------------------------------------------------------------
var alerts = document.querySelectorAll('.alert-dismissible');
var inputs = document.querySelectorAll('.myInputs')
var messages = document.querySelectorAll('.form-helper')
var forms = document.querySelectorAll('.form-outline')
// ---------------------------------------------------------------
// ESCONDER ALERTAS
// ---------------------------------------------------------------
alerts.forEach(function (alert) {
  setTimeout(function() {
      alert.classList.add('hide-me')
  }, 3000)
})
// ---------------------------------------------------------------
// ESCONDER MENSAGENS DE ERRO IMPUTS
// ---------------------------------------------------------------
messages.forEach(function (item) {
  setTimeout(function() {
      item.classList.add('hide-me')
  }, 3000)
})
// ---------------------------------------------------------------
// IMPUT INVALIDO
// ---------------------------------------------------------------
inputs.forEach(function (item) {
  item.addEventListener('change', (e)=>{
    target = e.target;
    if (!target.checkValidity()) {
      target.classList.add('myInputs-invalid')
    } else {
       target.classList.remove('myInputs-invalid')
    }
});
});


