//hamburger menu
const hamburger = document.querySelector(".c-hamburger")
const navlink = document.querySelector(".c-nav-links")

hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  navlink.classList.toggle("active");
});

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".nav-links a").forEach((link) => {
    link.addEventListener("click", () => {
      hamburger.classList.remove("active");
      navlink.classList.remove("active");
    });
  });
});



