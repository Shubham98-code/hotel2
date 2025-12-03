// Hotel Website JavaScript

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const navMenu = document.getElementById('nav-menu');
    
    if (mobileMenuBtn && navMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            navMenu.classList.toggle('active');
            
            // Change icon
            const icon = mobileMenuBtn.querySelector('i');
            if (navMenu.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });

        // Close mobile menu when clicking on links
        const navLinks = navMenu.querySelectorAll('.nav-link');
        navLinks.forEach(link => {
            link.addEventListener('click', function() {
                navMenu.classList.remove('active');
                const icon = mobileMenuBtn.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            });
        });

        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            const isClickInsideNav = navMenu.contains(event.target);
            const isClickOnButton = mobileMenuBtn.contains(event.target);
            
            if (!isClickInsideNav && !isClickOnButton && navMenu.classList.contains('active')) {
                navMenu.classList.remove('active');
                const icon = mobileMenuBtn.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Smooth scrolling for anchor links
    const anchorLinks = document.querySelectorAll('a[href^="#"]');
    anchorLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                const headerHeight = document.querySelector('.header').offsetHeight;
                const targetPosition = targetSection.offsetTop - headerHeight;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Add active class to navigation links based on scroll position
    const sections = document.querySelectorAll('section[id]');
    const navLinksForHighlight = document.querySelectorAll('.nav-link');

    function highlightNavigation() {
        const scrollPosition = window.scrollY + 100;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLinksForHighlight.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === `#${sectionId}`) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }

    // Add scroll event listener
    window.addEventListener('scroll', highlightNavigation);

    // // Contact form handling (if you add a form later)
    // function handleReservation() {
    //     alert('Thank you for your interest! We will contact you shortly to confirm your reservation.');
    // }

    // Add click handlers to reservation buttons
    const reservationButtons = document.querySelectorAll('.btn');
    reservationButtons.forEach(button => {
        if (button.textContent.includes('Reserve') || 
            button.textContent.includes('Book') || 
            button.textContent.includes('Make a Reservation')) {
            button.addEventListener('click', handleReservation);
        }
    });

    // Scroll animations
    function animateOnScroll() {
        const elements = document.querySelectorAll('.feature-card, .contact-card, .amenity-item');
        
        elements.forEach(element => {
            const elementTop = element.getBoundingClientRect().top;
            const elementVisible = 150;
            
            if (elementTop < window.innerHeight - elementVisible) {
                element.classList.add('fade-in-up');
            }
        });
    }

    // Add scroll event for animations
    window.addEventListener('scroll', animateOnScroll);
    
    // Run once on load
    animateOnScroll();

    // Header background on scroll
    const header = document.querySelector('.header');
    function updateHeaderBackground() {
        if (window.scrollY > 100) {
            header.style.backgroundColor = 'rgba(253, 246, 240, 0.98)';
        } else {
            header.style.backgroundColor = 'rgba(253, 246, 240, 0.95)';
        }
    }

    window.addEventListener('scroll', updateHeaderBackground);

    // Simple Excel data simulation for future integration
    const hotelData = {
        reservations: [],
        rooms: [
            { id: 1, type: 'Deluxe', price: 299, available: true },
            { id: 2, type: 'Suite', price: 599, available: true },
            { id: 3, type: 'Presidential', price: 999, available: true }
        ],
        bookings: []
    };

    // Function to simulate saving data to Excel (placeholder)
    function saveToExcel(data, type) {
        console.log(`Saving ${type} data:`, data);
        // In a real implementation, this would interface with a backend service
        // that writes to an Excel file or converts data to Excel format
        alert(`Data saved successfully! In a real implementation, this would be saved to an Excel file.`);
    }

    // Example reservation function
    function makeReservation(customerData) {
        const reservation = {
            id: Date.now(),
            customer: customerData,
            date: new Date().toISOString(),
            status: 'pending'
        };
        
        hotelData.reservations.push(reservation);
        saveToExcel(reservation, 'reservation');
        return reservation;
    }

    // Expose functions globally for potential form integration
    window.hotelFunctions = {
        makeReservation,
        saveToExcel,
        hotelData
    };

    console.log('Hotel website loaded successfully!');
    console.log('Excel integration functions available in window.hotelFunctions');
});
