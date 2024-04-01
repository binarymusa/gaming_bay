

document.addEventListener('scroll', function(){
    var vagueElements = document.querySelectorAll('#vague');

    vagueElements.forEach(function(element) {
        if (isElementInViewport(element)) {
            element.style.opacity = '1';
        } else {
            element.style.opacity = '0.2';
        }
    });
});

// Function to check if an element is in the viewport
function isElementInViewport(el) {
    var rect = el.getBoundingClientRect();
    return (
        rect.top >= 0 &&
        rect.left >= 0 &&
        rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
        rect.right <= (window.innerWidth || document.documentElement.clientWidth)
    );
}

