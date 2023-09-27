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
      if (window.pageYOffset < 200) {
        navLinks[0].classList.add('active');
        // miniNavLinks[0].classList.add('active-mini');
      } else {
        navLinks[index].classList.add('active');
        // miniNavLinks[index].classList.add('active-mini');
      }
    }
  });
});

const nameInput = document.getElementById("name-input");
const emailInput = document.getElementById("email-input");
const subjectInput = document.getElementById("subject-input");
// const sendButton = document.querySelector(".send-button");
// Function to handle the "Send" button click
function handleSendButtonClick() {

  if (nameInput.value && emailInput.value && subjectInput.value) {
    // Change the button text to "Sent!" and disable it
    sendButton.textContent = "Sent!";
    sendButton.style.color = "lightgreen"; // Change the text color to green
    sendButton.style.borderColor = "lightgreen";
    sendButton.disabled = true;

    // After 5 seconds, revert the button text and re-enable it
    setTimeout(function () {
      sendButton.textContent = "Send";
      sendButton.disabled = false;
      sendButton.style.color = "white";
      sendButton.style.borderColor = "white";
    }, 6000); // 5000 milliseconds (5 seconds)
  }
  if (!nameInput.value || !emailInput.value || !subjectInput.value) {
    window.alert("Please fill all fields to send message!")
  }
}
const sendButton = document.querySelector(".send-button");
sendButton.addEventListener("click", handleSendButtonClick);




const clicked = document.getElementById("sender");
clicked.addEventListener('click',function(e){
   e.preventDefault();
   sendMail();
});

function sendMail(){
   var params = {
       name : document.getElementById('name-input').value,
       email : document.getElementById('email-input').value,
       subject : document.getElementById('subject-input').value,
       message : document.getElementById('message-input').value,
       
   };
  const serviceID = "service_sqx3jo3";
  const tempID = "template_57rdyzu";
  if (nameInput.value && emailInput.value && subjectInput.value) {
    emailjs.send(serviceID,tempID,params)
    .then((res)=>{
      document.getElementById('name-input').value= ""
      document.getElementById('email-input').value= ""
      document.getElementById('subject-input').value= ""
      document.getElementById('message-input').value= ""
    })
  }
}



function updateBackgroundHeights() {
  const pageHeight = Math.min(document.body.scrollHeight, document.body.offsetHeight);
  const elements = document.querySelectorAll('.stars, .twinkling, .clouds');
  elements.forEach(element => {
      element.style.height = pageHeight + 'px';
  });
}

// Call the function initially and whenever the window is resized
updateBackgroundHeights();
window.addEventListener('resize', updateBackgroundHeights);



// Get all image elements with class "image-src-proj"
const projectImages = document.querySelectorAll(".image-src-proj");
const modal = document.getElementById("myModal");
const modalImg = document.getElementById("img01");
const captionText = document.getElementById("caption");
const closeModal = document.getElementById("close");

// Function to open the modal with the clicked image
function openModal(imageSrc, altText) {
  modal.style.display = "block";
  modalImg.src = imageSrc;
  captionText.innerHTML = altText;
  document.body.style.overflow = "hidden"; 
}

// Add click event listeners to all project images
projectImages.forEach((image, index) => {
  image.addEventListener("click", () => {
    const imageSrc = image.src;
    const altText = image.alt;
    openModal(imageSrc, altText);
  });
});

// Close modal when the close button is clicked
// closeModal.addEventListener("click", () => {
//   modal.style.display = "none";
// });


document.addEventListener("click", (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
    document.body.style.overflow = "auto";
  }
});

// Close modal when the navigation bar is clicked
const navbar = document.getElementsByTagName("nav")[0];
navbar.addEventListener("click", () => {
  modal.style.display = "none";
  document.body.style.overflow = "auto"; 
});


document.addEventListener("touchstart", (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
    document.body.style.overflow = "auto";
  }
});



// // Get all skill-list elements
// const skillLists = document.querySelectorAll(".skill-list");
// skillLists.forEach((skillList) => {
//   skillList.addEventListener("click", () => {
//     skillList.classList.toggle("active");
//   });
// });
