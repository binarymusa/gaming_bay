

// document.addEventListener('DOMContentLoaded', function() {
//     var alert = document.querySelector('.alert');

//     setTimeout(function() {
//         alert.parentNode.removeChild(alert);
//     }, 4000); // Change 5000 to the desired time in milliseconds
// });

// document.addEventListener('DOMContentLoaded', function() {
//     function adjustAlertPosition() {
//         var alert = document.getElementById('.alert');
//         var screenWidth = window.innerWidth;
//         var alertWidth = alert.offsetWidth;
//         var leftOffset = (screenWidth - alertWidth) / 2;
//         alert.style.left = leftOffset + 'px';
//     }

//     adjustAlertPosition(); // Call the function initially

//     // Listen for window resize events to readjust position
//     window.addEventListener('resize', adjustAlertPosition);
// })

document.addEventListener('DOMContentLoaded', function(){
    var alert = document.querySelector('.alert');    
    setTimeout(function() {
        alert.parentNode.removeChild(alert);
    }, 4000);

    function newOpacity() {
        alert.style.opacity = '1';
    }
    function oldOpacity(){
        alert.style.opacity = ''
    }

   alert.addEventListener('mouseenter', newOpacity());
   alert.addEventListener('mouseleave', oldOpacity());
})