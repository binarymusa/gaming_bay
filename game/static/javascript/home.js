
// wait for page to load
document.addEventListener('DOMContentLoaded', function(){    
    // get the target element(class or id)
    paragraphs.forEach(function(paragraph) {
        var text = paragraph.textContent.trim();
        paragraph.innerHTML = ''; // Clear content

        var i = 0; // word counter initializer

        var lineHeight = parseInt(window.getComputedStyle(paragraph).lineHeight);
        var containerWidth = paragraph.parentNode.offsetWidth;

        var lineCount = 0; // line counter initializer
        var lineText = ''; // variable to store text for each line

        var typingInterval = setInterval(function() {
            if (i < text.length) {
                lineText += text.charAt(i);
                i++;
            }

            // stop writing if all words have been iterated over
            if (i === text.length) {
                clearInterval(typingInterval);
            }

            // Check if the line exceeds the container width
            for (var i = 0; i < text.length; i++) {
                lineText += text.charAt(i);
    
                // Check if the line exceeds the container width or if it's at the end of the text
                if (paragraph.offsetWidth > containerWidth || i === text.length - 1) {
                    var lineSpan = document.createElement('span');
                    lineSpan.textContent = lineText.trim(); // Set the text content of the span
                    paragraph.appendChild(lineSpan); // Append the span to the paragraph
                    paragraph.appendChild(document.createElement('br')); // Add a line break
                    lineText = ''; // Clear line text for the next line
                }
            }
        }
    )}, 100); // typing speed is adjusted here
});


