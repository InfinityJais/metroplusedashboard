// Smooth scrolling for navigation links
document.querySelectorAll('nav a').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const section = document.querySelector(this.getAttribute('href'));
        section.scrollIntoView({ behavior: 'smooth' });
    });
});

// Optional: Add a subtle fade-in effect on scroll
window.addEventListener('scroll', () => {
    const cards = document.querySelectorAll('.content-card');
    cards.forEach(card => {
        const speed = 200;
        const top = card.getBoundingClientRect().top;
        if (top < window.innerHeight - speed) {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }
    });
});

// Initialize card styles for animation
document.querySelectorAll('.content-card').forEach(card => {
    card.style.opacity = '0';
    card.style.transform = 'translateY(30px)';
    card.style.transition = 'all 0.6s ease-out';
});