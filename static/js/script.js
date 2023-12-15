const slider = document.querySelector('.slider');

function activate(e) {
  const items = document.querySelectorAll('.item');
  e.target.matches('.next') && slider.append(items[0])
  e.target.matches('.prev') && slider.prepend(items[items.length-1]);
}

document.addEventListener('click',activate,false);

/* function redirectToPage(pageName) {
  // Utiliza Flask para redirigir a la página correspondiente
  var url = "{{ url_for('templates', filename=/paginaMUAC.html) }}";
  window.location.href = url;
}

document.addEventListener('click', function (event) {
    if (event.target.matches('.content button')) {
      // Encuentra el elemento padre 'item' para obtener el nombre de la página
      var item = event.target.closest('.item');
      if (item) {
        var pageName = item.querySelector('.title').innerText.toLowerCase();
        redirectToPage(pageName);
      }
    }
  }, false); */