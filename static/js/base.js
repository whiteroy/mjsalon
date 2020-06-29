function btncitas() {
  document.getElementById("btncitas").classList.toggle("show");
}

function btnventas() {
  document.getElementById('btnventas').classList.toggle('show');
}

function btninventario() {
  document.getElementById('btninventario').classList.toggle('show');
}

function btncatalogos() {
  document.getElementById('btncatalogos').classList.toggle('show');
}

function btnclientes() {
  document.getElementById('btnclientes').classList.toggle('show');
}

function btnusuarios() {
  document.getElementById('btnusuarios').classList.toggle('show');
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches('.icon, .btn')) {
    var dropdowns = document.getElementsByClassName("dropdown-menu");
    for (let i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}