/*
  layout.js
  This file contains the shared HTML for the footer,
  and the JavaScript for mobile menu and active link highlighting.
  
  NOTE: The header is now rendered by Django using {% include 'header.html' %}.
*/

// --- 1. HTML CONTENT ---

// 🛑 DELETED: The 'headerHTML' constant is removed to stop the static header injection.

// Footer HTML (kept as is)
const footerHTML = `
<footer class="bg-amber-100 border-t border-amber-200 section-container">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-8">
            <div class="js-animate js-from-up content-block-hover" style="transition-delay: 0.1s;">
                <div class="flex items-center gap-3 mb-4">
                    <img src="/static/css/logo.png" alt="The Gupta Hotel" class="h-12 w-12 object-contain" />
                    <span class="text-xl font-bold text-gray-900">The Gupta Hotel</span>
                </div>
                <p class="text-gray-700 mb-4">Where luxury meets culinary excellence. Experience the finest in hospitality and dining.</p>
                <div class="flex items-center gap-2 text-amber-700 font-semibold">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="currentColor" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-star"><path d="M11.525 2.295a.53.53 0 0 1 .95 0l2.31 4.679a2.123 2.123 0 0 0 1.595 1.16l5.166.756a.53.53 0 0 1 .294.904l-3.736 3.638a2.123 2.123 0 0 0-.611 1.878l.882 5.14a.53.53 0 0 1-.771.56l-4.618-2.428a2.122 2.122 0 0 0-1.973 0L6.396 21.01a.53.53 0 0 1-.77-.56l.881-5.139a2.122 2.122 0 0 0-.611-1.879L2.16 9.795a.53.53 0 0 1 .294-.906l5.165-.755a2.122 2.122 0 0 0 1.597-1.16z"/></svg>
                    5-Star Rating
                </div>
            </div>

            <div class="js-animate js-from-up content-block-hover" style="transition-delay: 0.2s;">
                <h3 class="text-lg font-bold text-gray-900 mb-4">Quick Links</h3>
                <ul class="space-y-3">
                    <li class="hover:translate-x-1 transition-transform duration-300"><a href="/" class="text-gray-700 hover:text-amber-700 transition-colors">Home</a></li>
                    <li class="hover:translate-x-1 transition-transform duration-300"><a href="/about" class="text-gray-700 hover:text-amber-700 transition-colors">About Us</a></li>
                    <li class="hover:translate-x-1 transition-transform duration-300"><a href="/rooms" class="text-gray-700 hover:text-amber-700 transition-colors">Rooms & Suites</a></li>
                    <li class="hover:translate-x-1 transition-transform duration-300"><a href="/contact" class="text-gray-700 hover:text-amber-700 transition-colors">Contact Us</a></li>
                </ul>
            </div>

            <div class="js-animate js-from-up content-block-hover" style="transition-delay: 0.3s;">
                <h3 class="text-lg font-bold text-gray-900 mb-4">Contact Info</h3>
                <ul class="space-y-3">
                    <li class="flex items-start gap-3">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-phone text-amber-700 flex-shrink-0 mt-0.5"><path d="M13.832 16.568a1 1 0 0 0 1.213-.303l-.355-.465A2 2 0 0 1 17 15h3a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2A18 18 0 0 1 2 4a2 2 0 0 1 2-2h3a2 2 0 0 1 2 2v3a2 2 0 0 1-.8 1.6l-.468.351a1 1 0 0 0-.292 1.233 14 14 0 0 0 6.392 6.384"/></svg>
                        <div>
                            <p class="text-gray-700">+91 9835364361</p>
                            <p class="text-gray-700">+91 7644894498</p>
                        </div>
                    </li>
                    <li class="flex items-start gap-3">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-mail text-amber-700 flex-shrink-0 mt-0.5"><path d="m22 7-8.991 5.727a2 2 0 0 1-2.009 0L2 7"/><rect x="2" y="4" width="20" height="16" rx="2"/></svg>
                        <p class="text-gray-700">info@guptahotel.com</p>
                    </li>
                    <li class="flex items-start gap-3">
                        <svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="lucide lucide-map-pin text-amber-700 flex-shrink-0 mt-0.5"><path d="M20 10c0 4.993-5.539 10.193-7.399 11.799a1 1 0 0 1-1.202 0C9.539 20.193 4 14.993 4 10a8 8 0 0 1 16 0"/><circle cx="12" cy="10" r="3"/></svg>
                        <p class="text-gray-700">
                            Stila Mander, Near Sabji Mandi<br>
                            Jamshedpur, Sakchi, 831001<br>
                            Jharkhand
                        </p>
                    </li>
                </ul>
            </div>
        </div>
        <div class="border-t border-amber-200 pt-8 text-center text-gray-700 js-animate js-from-up" style="transition-delay: 0.3s;">
            <p>© 2025 The Gupta Hotel. All rights reserved.</p>
        </div>
    </div>
</footer>
`;


// --- 2. INJECTION & LOGIC ---

/**
 * Injects the footer, sets up menu logic, and highlights the active nav link.
 */
function injectLayout() {
    // 🛑 REMOVED: const headerPlaceholder = document.getElementById('header-placeholder');
    const footerPlaceholder = document.getElementById('footer-placeholder');

    // 🛑 DELETED: The static header injection block was here.

    // Inject Footer HTML (This remains)
    if (footerPlaceholder) {
        footerPlaceholder.innerHTML = footerHTML;
    }

    // --- Mobile Menu Logic (now runs on the Django-rendered header) ---
    const menuToggle = document.getElementById('menu-toggle');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuIcon = document.getElementById('menu-icon');
    const closeIcon = document.getElementById('close-icon');
    
    let isMenuOpen = false;

    function openMenu() {
        if (isMenuOpen || !mobileMenu || !menuIcon || !closeIcon) return;
        isMenuOpen = true;
        mobileMenu.classList.remove('hidden');
        mobileMenu.classList.add('mobile-menu-enter');
        menuIcon.classList.add('hidden');
        closeIcon.classList.remove('hidden');
    }

    function closeMenu() {
        if (!isMenuOpen || !mobileMenu || !menuIcon || !closeIcon) return;
        isMenuOpen = false;
        mobileMenu.classList.add('mobile-menu-exit');
        mobileMenu.classList.remove('mobile-menu-enter');
        
        mobileMenu.addEventListener('animationend', function handler() {
            mobileMenu.classList.add('hidden');
            mobileMenu.classList.remove('mobile-menu-exit');
            menuIcon.classList.remove('hidden');
            closeIcon.classList.add('hidden');
            mobileMenu.removeEventListener('animationend', handler);
        }, {once: true});
    }

    if (menuToggle) {
        menuToggle.addEventListener('click', () => {
            if (isMenuOpen) {
                closeMenu();
            } else {
                openMenu();
            }
        });
    }

    // Make closeMenu globally accessible for the inline 'onclick' attributes
    window.closeMenu = closeMenu;

    // --- Active Link Logic ---
    const path = window.location.pathname; // e.g., "/", "/about", "/rooms"
    let activePage = 'home'; // Default to home

    // Determine active page based on URL
    if (path.startsWith('/contact')) {
        activePage = 'contact';
    } else if (path.startsWith('/about')) {
        activePage = 'about';
    } else if (path.startsWith('/rooms')) {
        activePage = 'rooms';
    } else if (path === '/') {
        activePage = 'home';
    }

    // Find all nav links (desktop and mobile)
    const navLinks = document.querySelectorAll(`[data-nav-link]`);
    
    navLinks.forEach(link => {
        const linkPage = link.getAttribute('data-nav-link');
        const underline = link.querySelector('.nav-underline'); // Desktop only

        if (linkPage === activePage) {
            // Add active styles
            link.classList.remove('text-gray-700', 'hover:text-amber-600', 'font-medium');
            link.classList.add('text-amber-600', 'font-bold');
            // Add underline for active desktop link
            if (underline) {
                underline.classList.remove('w-0');
                underline.classList.add('w-full');
            }
        } else {
            // Ensure inactive styles
            link.classList.add('text-gray-700', 'hover:text-amber-600', 'font-medium');
            link.classList.remove('text-amber-600', 'font-bold');
            // Remove underline for inactive desktop link
            if (underline) {
                underline.classList.add('w-0');
                underline.classList.remove('w-full');
            }
        }
    });
}

// --- 3. EXECUTION ---

// Run the injection function once the DOM is ready
document.addEventListener('DOMContentLoaded', injectLayout);