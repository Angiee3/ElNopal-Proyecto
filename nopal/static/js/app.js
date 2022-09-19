// var swiper = new Swiper('.swiper-container', {
// 	navigation: {
// 	  nextEl: '.swiper-button-next',
// 	  prevEl: '.swiper-button-prev'
// 	},
// 	slidesPerView: 1,
// 	spaceBetween: 1,
// 	// init: false,
// 	pagination: {
// 	  el: '.swiper-pagination',
// 	  clickable: true,
// 	},

  
// 	breakpoints: {
// 	  620: {
// 		slidesPerView: 1,
// 		spaceBetween: 20,
// 	  },
// 	  680: {
// 		slidesPerView: 2,
// 		spaceBetween: 40,
// 	  },
// 	  920: {
// 		slidesPerView: 3,
// 		spaceBetween: 40,
// 	  },
// 	  1240: {
// 		slidesPerView: 4,
// 		spaceBetween: 50,
// 	  },
// 	} 
//     });
const gliders = document.querySelectorAll("[id^=glider]");

gliders.forEach((glide) => {
    const glider = document.querySelector(`#${glide.id} .glider`);
  const gliderPrev = document.querySelector(`#${glide.id} .glider-prev`);
  const gliderNext = document.querySelector(`#${glide.id} .glider-next`);
  const gliderDots = document.querySelector(`#${glide.id} .dots`);

    new Glider(glider, {
        slidesToShow: 3,
        draggable: true,
        dots: gliderDots,
		clickable: true,

        arrows: {
          prev: gliderPrev,
          next: gliderNext
        }
      });
    });