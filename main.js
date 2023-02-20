window.addEventListener('scroll', function() {
    let header = document.getElementById('header');
    if (window.pageYOffset > 60) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});




const mq = window.matchMedia("(min-width: 786px)");
const smallBack = document.querySelector(".background");
window.addEventListener("resize", function() {
  if (mq.matches) {
    smallBack.style.display = "none";
  }
});

const hamburger = document.querySelector('.fa-bars');
const xMark = document.querySelector(".fa-times");
const dropCont = document.querySelector('.small-nav-drop-cont');
const background = document.querySelector('.background');
xMark.style.display = "none";
dropCont.style.display = "none";
background.style.display = "none";
hamburger.addEventListener('click', function() {
    dropCont.style.display = "flex";
    background.style.display = "block";
    xMark.style.display = "";
    hamburger.style.display = "none";
});

xMark.addEventListener('click', function() {
  dropCont.style.display = "none";
  background.style.display = "none";
  xMark.style.display = "none";
  hamburger.style.display = "";
});

const miniNavLinks = document.querySelectorAll(".mini-nav-link");
const smallNav = document.querySelector(".small-nav-drop-cont");

for (let i = 0; i < miniNavLinks.length; i++) {
  miniNavLinks[i].addEventListener("click", function() {
    console.log("CLICK");
    smallNav.style.display = "none";
    smallBack.style.display = "none";
    xMark.style.display = "none";
    hamburger.style.display = "block";
  });
};

const miniProjDrop = document.getElementById("mini-project-drop");
const miniProjects = document.getElementById("mini-project-dropdown");
const downArrow = document.querySelector(".fa-chevron-down");
const upArrow = document.querySelector(".fa-chevron-up");
downArrow.style.display = "none";
miniProjects.style.display = "none";
miniProjDrop.addEventListener("click", function() {
  if(miniProjects.style.display === "none"){
    miniProjects.style.display = "flex";
    miniProjects.style.flexDirection = "column";
    upArrow.style.display = "none";
    downArrow.style.display = "";
  }
  else {
    miniProjects.style.display = "none";
    upArrow.style.display = "";
    downArrow.style.display = "none";
  }
});

const miniProjectDrop = document.querySelector('#mini-project-drop');
const miniProjectDropdown = document.querySelector('.mini-project-dropdown-container');
const belowLinks = document.querySelectorAll('.below');
miniProjectDrop.addEventListener('click', () => {
  if (miniProjectDropdown.classList.contains('show')) {
    miniProjectDropdown.classList.remove('show');
    belowLinks.forEach(link => link.classList.remove('moved-down'));
    belowLinks.forEach(link => link.classList.add('moved-up'));
  } else {
    miniProjectDropdown.classList.add('show');
    belowLinks.forEach(link => link.classList.add('moved-down'));
    belowLinks.forEach(link => link.classList.remove('moved-up'));
  }
});




function filterProjects(tag) {
  // Get all the project elements
  var projects = document.querySelectorAll(".projects-list");
  // Hide all the projects
  for (var i = 0; i < projects.length; i++) {
    projects[i].style.display = "none";
  }
  // Show only the projects that match the selected tag or programming language
  if (tag === "all") {
    for (var i = 0; i < projects.length; i++) {
      projects[i].style.display = "grid";
    }
  } else {
    for (var i = 0; i < projects.length; i++) {
      if ( projects[i].dataset.tags.includes(tag) || projects[i].classList.contains(tag)) {
          projects[i].style.display = "grid";
      }
    }
  }
}


// Stroke on Scroll
const sections = document.querySelectorAll('.section-start');
const navLinks = document.querySelectorAll('.nav-link');
function isInViewport(element) {
  const rect = element.getBoundingClientRect();
  return (
    rect.top >= 0 &&
    rect.left >= 0 &&
    rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
    rect.right <= (window.innerWidth || document.documentElement.clientWidth)
  );
}
window.addEventListener('scroll', function() {
  sections.forEach((section, index) => {
    if (isInViewport(section)) {
      navLinks.forEach(navLink => navLink.classList.remove('active'));
      // miniNavLinks.forEach(navLink => navLink.classList.remove('active-mini'));
      if (index === 0 || window.pageYOffset < 200) {
        navLinks[0].classList.add('active');
        // miniNavLinks[0].classList.add('active-mini');
      } else {
        navLinks[index].classList.add('active');
        // miniNavLinks[index].classList.add('active-mini');
      }
    }
  });
});


