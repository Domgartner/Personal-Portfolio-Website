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