//year
const year = new Date()
document.getElementById("current-year").textContent = year.toLocalString();
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

function openWhatsApp() { 
  const phone = "+917598090156";
   const message = encodeURIComponent("Hi, I need assistance!"); 
   window.open(`https://wa.me/${phone}?text=${message}`, "_blank");
}

