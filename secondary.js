let slideIndex = 0;
let timeoutId;
showSlides();
function showSlides(index) {
  let i;
  let slides = document.getElementsByClassName("mySlides");
  let dots = document.getElementsByClassName("dot");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";  
  }
  if (index !== undefined) {
    slideIndex = index;
  } else {
    slideIndex++;
    if (slideIndex > slides.length) {
      slideIndex = 1;
    }    
  }
  for (i = 0; i < dots.length; i++) {
    dots[i].className = dots[i].className.replace(" active-dot", "");
  }
  slides[slideIndex-1].style.display = "block";  
  dots[slideIndex-1].className += " active-dot";
  clearTimeout(timeoutId);
  timeoutId = setTimeout(showSlides, 7800); 
}

let dotElements = document.getElementsByClassName("dot");
for (let i = 0; i < dotElements.length; i++) {
  dotElements[i].addEventListener("click", function() {
    showSlides(i+1);
  });
}


  // let slideIndexBlog = 0;
  // let timeoutIdBlog;
  // showSlidesBlog();
  // function showSlidesBlog(index) {
  //   let i;
  //   let slides = document.getElementsByClassName("mySlides-blog");
  //   let dots = document.getElementsByClassName("dot");
  //   for (i = 0; i < slides.length; i++) {
  //     slides[i].style.display = "none";  
  //   }
  //   if (index !== undefined) {
  //     slideIndexBlog = index;
  //   } else {
  //     slideIndexBlog++;
  //     if (slideIndexBlog > slides.length) {
  //       slideIndexBlog = 1;
  //     }    
  //   }
  //   for (i = 0; i < dots.length; i++) {
  //     dots[i].className = dots[i].className.replace(" active-dot", "");
  //   }
  //   slides[slideIndexBlog-1].style.display = "block";  
  //   dots[slideIndexBlog-1].className += " active-dot";
  //   clearTimeout(timeoutIdBlog);
  //   timeoutIdBlog = setTimeout(showSlides, 7800); 
  // }
  
  // let dotElementsBlog = document.getElementsByClassName("dot");
  // for (let i = 0; i < dotElements.length; i++) {
  //   dotElementsBlog[i].addEventListener("click", function() {
  //     showSlides(i+1);
  //   });
  // }

  

  // Get all elements with class "slideshow-image"
const slideshowImages = document.querySelectorAll(".slideshow-image");

// Add click event listeners to open the modal for each image
slideshowImages.forEach((image) => {
  image.addEventListener("click", () => {
    openModal(image.src, image.alt);
  });
});

// Close modal when clicking outside of the modal content
// closeModal.addEventListener("click", () => {
//   modal.style.display = "none";
// });

window.addEventListener("click", (event) => {
  if (event.target === modal) {
    modal.style.display = "none";
  }
});





// let currentIndex = 0;
// let images = document.querySelectorAll(".slideshow-image");

// function openModal(imageIndex) {
//   modal.style.display = "block";
//   modalImg.src = images[imageIndex].src;
//   captionText.innerHTML = images[imageIndex].alt;
//   currentIndex = imageIndex;
// }

// function plusSlides(n) {
//   let newIndex = currentIndex + n;

//   if (newIndex < 0) {
//     newIndex = images.length - 1;
//   } else if (newIndex >= images.length) {
//     newIndex = 0;
//   }

//   openModal(newIndex);
// }

// let prevButton = document.querySelector(".prev");
// let nextButton = document.querySelector(".next");

// prevButton.addEventListener("click", function () {
//   plusSlides(-1);
// });

// nextButton.addEventListener("click", function () {
//   plusSlides(1);
// });

// // Close modal when clicking outside of the modal content
// window.addEventListener("click", function (event) {
//   if (event.target === modal) {
//     closeModal();
//   }
// });


