// Get the container holding the checkboxes
const checkboxContainer = document.getElementById('checkbox-topics');

// Add a single change event listener to the container
checkboxContainer.addEventListener('change', function() {
    // Select all checkboxes inside the container
    const checkboxes = checkboxContainer.querySelectorAll('input[type="checkbox"]');

    // Loop through each checkbox to control visibility of elements
    checkboxes.forEach((checkbox) => {
        // Get all elements with a class name matching the checkbox value
        const elements = document.querySelectorAll(`.${checkbox.value}`);
        
        // Show or hide elements based on checkbox state
        elements.forEach((element) => {
            element.style.display = checkbox.checked ? 'block' : 'none';
        });
    });
});
