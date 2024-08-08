//function loginSubmit() {
//  let loginUsername = document.getElementById("loginusername").value;
//  let loginPassword = document.getElementById("loginpassword").value;
//
//  console.log("Log In Submit: " + loginUsername + loginPassword);
//
//  document.getElementById("loginusername").value = "";
//  document.getElementById("loginpassword").value = "";
//}
//
//function registerSubmit() {
//  let registerUsername = document.getElementById("registerusername").value;
//  let registerPassword = document.getElementById("registerpassword").value;
//  let confirmPassword = document.getElementById("confirmpassword").value;
//  const errorElement = document.getElementById('passwordError');
//
//  console.log(
//    "Log In Submit: " +
//      registerUsername +
//      ":" +
//      registerPassword +
//      ":" +
//      confirmPassword
//  );
//
//  document.getElementById("registerusername").value = "";
//  document.getElementById("registerpassword").value = "";
//  document.getElementById("confirmpassword").value = "";
//
//  if (registerPassword !== confirmPassword) {
//      errorElement.textContent = 'Passwords do not match';
//  } else {
//    fetch(`${window.origin}/registration`,{
//                method : "POST"
//            }).then(function(response)
//            {
//                if(response.status!=200)
//                {
//                    console.log("");
//                }
//                response.json().then(function(data)
//                {
//                    console.log(data);
//                });
//            }).catch(function(error)
//            {
//                console.log(error);
//            });
//  }
//
//}

(function ($) {
   "use strict";
   console.log("Swiper Function");
   $(document).ready(function () {
     var mainSwiper = new Swiper(".main-swiper", {
       autoplay: {
          delay: 5000,
        },
       speed: 600,
       navigation: {
         nextEl: ".main-slider-button-next",
         prevEl: ".main-slider-button-prev",
       },
     });
   });
})(jQuery);
