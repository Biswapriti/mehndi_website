// Hamburger menu toggle functionality
const menu = document.getElementById('menu');
const nav = document.querySelector('.right ul');

menu.addEventListener('click', () => {
    nav.classList.toggle('nav-toggle');
});

// Back to Top Button Functionality
const backToTopButton = document.getElementById('backToTop');

// Show the button when scrolling down
window.onscroll = function () {
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
        backToTopButton.style.display = 'block';
    } else {
        backToTopButton.style.display = 'none';
    }
};

// Scroll to the top when the button is clicked
backToTopButton.onclick = function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
};