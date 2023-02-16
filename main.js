window.addEventListener('scroll', function() {
    let header = document.getElementById('header');
    if (window.pageYOffset > 60) {
        header.classList.add('scrolled');
    } else {
        header.classList.remove('scrolled');
    }
});


// window.addEventListener('scroll', function() {
//     let header = document.getElementById('header');
//     let projectDropdown = document.getElementById('project-dropdown');
//     if (window.pageYOffset > 60) {
//         header.classList.add('scrolled');
//         projectDropdown.classList.add('scrolled');
//     } else {
//         header.classList.remove('scrolled');
//         projectDropdown.classList.remove('scrolled');
//     }
// });



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
      if (index === 0 || window.pageYOffset < 200) {
        navLinks[0].classList.add('active');
      } else {
        navLinks[index].classList.add('active');
      }
    }
  });
});





const prev = document.querySelector('.fa-arrow-right');
const next = document.querySelector('.fa-arrow-left');
const images = document.querySelector('.carousel').children;
const totalImages = images.length;
let index = 0;
prev.addEventListener('click', () => {
  nextImage('next');
})
next.addEventListener('click', () => {
  nextImage('prev');
})
function nextImage(direction) {
  if(direction == 'next') {
    index++;
    if(index == totalImages) {
      index = 0;
    }
  } else {
    if(index == 0) {
      index = totalImages - 1;
    } else {
      index--;
    }
  }
  for(let i = 0; i < images.length; i++) {
    images[i].classList.remove('main');
  }
  images[index].classList.add('main');
}