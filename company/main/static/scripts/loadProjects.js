document.addEventListener("DOMContentLoaded", function () {
    var loadMoreBtn = document.getElementById("load-more-btn");
    var projects = document.querySelectorAll(".project-card");
    var projectsToShow = 8;
    var index = projectsToShow;

    function hideProjects(start, end) {
        for (var i = start; i < end; i++) {
            if (projects[i]) {
                projects[i].style.display = "none";
            }
        }
    }

    function showProjects(start, end) {
        for (var i = start; i < end; i++) {
            if (projects[i]) {
                projects[i].style.display = "block";
            }
        }
    }

    // Скрываем все проекты, кроме первых 4
    hideProjects(projectsToShow, projects.length);

    // Если проектов меньше или равно 4, скрываем кнопку "More Projects"
    if (projects.length <= projectsToShow) {
        loadMoreBtn.style.display = "none";
    }

    loadMoreBtn.addEventListener("click", function (e) {
        // Предотвращаем стандартное действие кнопки (в данном случае, предотвращаем прокрутку наверх)
        e.preventDefault();
        // Показываем следующие 4 проекта
        showProjects(index, index + projectsToShow);
        index += projectsToShow;

        // Если больше нет проектов, скрываем кнопку "More Projects"
        if (index >= projects.length) {
            loadMoreBtn.style.display = "none";
        }
    });
});
