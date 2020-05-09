"use strict";

(function() {
    const els = [document.querySelector("h1"), ...document.querySelectorAll("h2")];
    const navLinks = document.querySelectorAll("nav div");

    function onScroll(evt) {
        for (let i = 0; i < els.length; i++) {
            const el = els[i];
            if (window.scrollY > el.offsetTop) {
                for (const link of navLinks) {
                    link.classList.remove("active");
                }
                navLinks[i].classList.add("active");
            }
        }
    }

    window.addEventListener('scroll', onScroll);
})();
