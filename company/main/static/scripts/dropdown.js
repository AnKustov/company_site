// JavaScript для открытия/закрытия выпадающего меню при наведении/убирании курсора
document.querySelectorAll(".nav-item.dropdown").forEach((dropdown) => {
  const dropdownToggle = dropdown.querySelector(".dropdown-toggle");
  const dropdownMenu = dropdown.querySelector(".dropdown-menu");

  dropdownToggle.addEventListener("mouseover", () => {
    dropdownMenu.classList.add("show");
  });

  dropdown.addEventListener("mouseleave", () => {
    dropdownMenu.classList.remove("show");
  });
});
