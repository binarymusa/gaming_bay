

document.addEventListener('change', function limitGamesSelection() {

    // get checkbox items
    var checkboxes = document.querySelectorAll('#textboxalter:checked');
    
    if (checkboxes.length >= 2) {
        // Disable unchecked checkboxes, 'not' is a negation item(reverses logic)
        var uncheckedCheckboxes = document.querySelectorAll('#textboxalter:not(:checked)');
        
        uncheckedCheckboxes.forEach(function(checkbox) {
            checkbox.disabled = true;
            
        });
    } else {
        // Enable all checkboxes
        var allCheckboxes = document.querySelectorAll('#textboxalter');

        allCheckboxes.forEach(function(checkbox) {
            checkbox.disabled = false;
        });
    }

});


// or you could use(remember to add the onchange event in the html specific area)

/* function limitGamesSelection() {

    // get checkbox items
    var checkboxes = document.querySelectorAll('input[name="games"]:checked');
    
    if (checkboxes.length >= 3) {
        // Disable unchecked checkboxes
        var uncheckedCheckboxes = document.querySelectorAll('input[name="games"]:not(:checked)');
        uncheckedCheckboxes.forEach(function(checkbox) {
            checkbox.disabled = true;
        });
    } else {
        // Enable all checkboxes
        var allCheckboxes = document.querySelectorAll('input[name="games"]');
        allCheckboxes.forEach(function(checkbox) {
            checkbox.disabled = false;
        });
    }
};
 */

