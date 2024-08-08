(function ($) {
  "use strict";

  $(document).ready(function () {
    var mainSwiper = new Swiper(".main-swiper", {
      speed: 500,
      navigation: {
        nextEl: ".main-slider-button-next",
        prevEl: ".main-slider-button-prev",
      },
    });
  });
})(jQuery);

function loginSubmit() {
  let loginUsername = document.getElementById("loginusername").value;
  let loginPassword = document.getElementById("loginpassword").value;

  console.log("Log In Submit: " + loginUsername + loginPassword);

  document.getElementById("loginusername").value = "";
  document.getElementById("loginpassword").value = "";
}
