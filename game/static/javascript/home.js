
// wait for page to load
document.addEventListener('DOMContentLoaded', function(){
    
    // get the target element(class or id)
    var paragraph = document.querySelector('.typewriter');

    // get the paragraph
    var text = paragraph.textContent;

    // clear the text content
    paragraph.textContent = '';

    // iterate through each character
    var i = 0;
    var typingInterval = setInterval( function() {
        paragraph.textContent += text.charAt(i); i++;

        // stop the interval when all characters are typed
        if (i === text.length) {
            clearInterval(typingInterval);
        }
    }, 100); // typing speed is adjusted here
});


// var timed = document.querySelector('#positon-1');

// function timer() {
//     timed.setTimeout(() => {
//         timed.style.display = "none";
//     }, 10);
// }