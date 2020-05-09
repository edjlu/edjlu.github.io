"use strict";

(function() {
    const modal = document.querySelector('.modal');

    function onClick(evt) {
        let container = evt.target;
        while (!container.classList.contains('container')) {
            container = container.parentElement;
        }
        const img = container.querySelector('img');

        const newImg = document.createElement('img');
        newImg.src = img.src;
        modal.childNodes.forEach((c) => modal.removeChild(c));
        modal.appendChild(newImg);
        modal.classList.add('active');
    }

    const thumbnails = document.querySelectorAll('.gallery > .container');
    for (const thumbnail of thumbnails) {
        thumbnail.addEventListener('click', onClick);
    }

    modal.addEventListener('click', () => {
        modal.classList.remove('active');
    });;
})();
