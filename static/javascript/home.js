// var navLinks = document.getElementById("navLinks")

// function showMenu(){
//     // sets the CSS right property of the navLinks element to "0"
//     navLinks.style.right = "0" 
// }

// function hideMenu(){
//     navLinks.style.right = "-200px"
// }

var navbar = document.getElementById('nav');
window.addEventListener('scroll', navcolor);

function navcolor(){
    if (window.scrollY > 0) {
        navbar.style.backgroundColor = "grey";
    } else {
        navbar.style.backgroundColor = "black";
    }

}




