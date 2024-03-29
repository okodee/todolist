document.addEventListener('DOMContentLoaded', function() {
    // This function will be executed when the DOM is fully loaded

    // Add your event listeners here
    const completedBtns = document.querySelectorAll('completed-btn');
  
    completedBtns.addEventListener('click', function() {
        // This function will be executed when the button is clicked
        console.log('Button clicked!');
    });
});