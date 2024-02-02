window.addEventListener('scroll', function () {
  var footer = document.getElementById('main-footer');
  var scrollPosition = window.innerHeight + window.scrollY;
  var footerPosition = footer.offsetTop;

  if (scrollPosition >= footerPosition) {
    footer.classList.add('visible');
  } else {
    footer.classList.remove('visible');
  }
});