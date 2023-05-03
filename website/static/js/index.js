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
// ---------------------------------------------------------------
// DELETAR NOTES
// ---------------------------------------------------------------
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
// ---------------------------------------------------------------
// ATUALIZAR USUARIO
// ---------------------------------------------------------------
  function atualizarUsuario(id, nome, email) {
    fetch("/atualizar-usuario", {
      method: "POST",
      body: JSON.stringify({ id: id, nome: nome, email: email }),
    }).then((_res) => {
      window.location.href = "/cadastro_usuarios";
    });
}
// ---------------------------------------------------------------
// DELETAR CLIENTE
// ---------------------------------------------------------------
  function deletarCliente(CliID) {
    fetch("/deletar-cliente", {
      method: "POST",
      body: JSON.stringify({ CliID: CliID }),
    }).then((_res) => {
      window.location.href = "/clientes";
    });
}





