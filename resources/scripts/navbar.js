var isToggled = false;
const navbar = document.getElementById("navbar");
const choices = document.getElementById("choices");
const hamburger = document.getElementById("hamburger");

const expandedChoicesClass = "choices-expanded"
const expandedNavbarClass = "navbar-expanded";



function toggleHamburger() {
    isToggled = !isToggled

    if (isToggled) { 
        navbar.classList.add(expandedNavbarClass);
        choices.classList.add(expandedChoicesClass);
        hamburger.src = "/resources/images/hamburger-close.png";
    } else {
        navbar.classList.remove(expandedNavbarClass);
        choices.classList.remove(expandedChoicesClass);
        hamburger.src = "/resources/images/hamburger-white.png";
    };

}