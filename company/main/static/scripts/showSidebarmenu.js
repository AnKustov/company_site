function toggleBlockVisibility(linkId, blockId) {
  var link = document.getElementById(linkId);
  var block = document.getElementById(blockId);

  if (link && block) {
    link.addEventListener("click", function (e) {
      e.preventDefault();
      var headerHeight = document.getElementById("main-header").offsetHeight;
      block.style.top = headerHeight + "px"; // Установка верхнего отступа
      block.classList.toggle("show-block");
    });

    document.addEventListener("click", function (e) {
      if (
        block.classList.contains("show-block") &&
        e.target !== link &&
        !block.contains(e.target)
      ) {
        block.classList.remove("show-block");
      }
    });
  }
}

// Добавляем обработчик события клика для ссылки "Contact"
toggleBlockVisibility("contact-link", "contact-block");


