const clientsCounter = document.getElementById("clientsCounter");
const yearsCounter = document.getElementById("yearsCounter");
const projectsCounter = document.getElementById("projectsCounter");


let clientsCount = 1;
let yearsCount = 1;
let projectsCount = 1;


function increaseClientsCounter() {
  if (clientsCount < 1234) {
    clientsCount++;
    clientsCounter.textContent = clientsCount;
  }
}

function increaseYearsCounter() {
  if (yearsCount < 30) {
    yearsCount++;
    yearsCounter.textContent = yearsCount;
  }
}

function increaseProjectsCounter() {
  if (projectsCount < 1786) {
    projectsCount++;
    projectsCounter.textContent = projectsCount;
  }
}

setInterval(increaseYearsCounter, 100);
setInterval(increaseClientsCounter, 0.1);
setInterval(increaseProjectsCounter, 0.05);

