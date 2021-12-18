function eliminarPalabra(palabra, significado) {
  fetch("/eliminar-palabra", {
    method: "POST",
    body: JSON.stringify({ palabra: palabra, significado: significado }),
  }).then((_res) => {
    window.location.href = "/";
  });
}
