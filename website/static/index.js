 // ************************************************************************************************** 
var alerts = document.querySelectorAll('.alert-dismissible');
var inputs = document.querySelectorAll('.myInputs')
var messages = document.querySelectorAll('.form-helper')
var forms = document.querySelectorAll('.form-outline')
// ESCONDE ALERTAS
alerts.forEach(function (alert) {
  setTimeout(function() {
      alert.classList.add('hide-me')
  }, 2000)
})
// ESCONDE MENSAGENS
messages.forEach(function (item) {
  setTimeout(function() {
      item.classList.add('hide-me')
  }, 2000)
})
// INPUT INVALIDO
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


// **************************************************************************************************
function deleteNote(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
// ---------------------------------------------------------------
// DELETAR USUARIO
// ---------------------------------------------------------------
  function deletarUsuario(UserID) {
    fetch("/deletar-usuario", {
      method: "POST",
      body: JSON.stringify({ UserID: UserID }),
    }).then((_res) => {
      window.location.href = "/usuarios";
    });
}

