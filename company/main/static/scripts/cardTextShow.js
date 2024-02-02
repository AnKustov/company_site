var cardTexts = document.querySelectorAll(".card-text"); // Получаем все элементы с классом "card-text"

var maxLength = 200; // Максимальное количество символов

cardTexts.forEach(function(cardText) {
  var originalText = cardText.textContent; // Сохраняем оригинальный текст

  if (originalText.length > maxLength) {
    // Если текст длиннее, чем максимальное количество символов
    var shortenedText = originalText.slice(0, maxLength) + "..."; // Обрезаем текст и добавляем многоточие
    cardText.textContent = shortenedText; // Заменяем текст в элементе
  }
});
