
var nav = document.getElementById("nav")

function showMenu(){
    // sets the CSS right property of the navLinks element to "0"
    nav.style.right = "0" 
}

function hideMenu(){
    nav.style.right = "-200px"
}




var counter = 1;
var increment = 1;

setInterval(function(){
    document.getElementById('radio' + counter).checked = true;
    counter += increment;
    if(counter > 6 || counter < 1){
        increment *= -1 ;
    }

    counter = Math.min(Math.max(counter, 1), 6);
}, 3000);



