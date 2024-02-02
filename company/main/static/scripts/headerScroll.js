window.addEventListener('scroll', function () {
    var navbar = document.querySelector('.navbar');
    if (window.scrollY > 100) { // высота скрола для изменения цвета 
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});