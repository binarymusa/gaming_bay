

var navBar = document.querySelector('.nav-bar ul');

function toggleMenu() {
    if (navBar.style.display === "block") {
        hideMenu();
    } else {
        showMenu();
    }
}

function showMenu(){
    navBar.style.display = "block"
}

function hideMenu(){
    navBar.style.display = "none" 
}


