'use strict';

const links = document.querySelectorAll('a');
const modal = document.querySelector('.modal');
const btnCloseModal = document.querySelector('.close-modal');
const p = document.querySelector('p');

const openModal = function () {
  modal.classList.remove('hidden');
};

const closeModal = function () {
  modal.classList.add('hidden');
  const para = document.querySelectorAll('p');
  para.forEach(el => {
    el.remove();
  });
};

btnCloseModal.addEventListener('click', closeModal);

document.addEventListener('keydown', function (e) {
  if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
    closeModal();
  }
});

links.forEach(element => {
  element.addEventListener('click', function (e) {
    e.preventDefault();
    const span = document.createElement("span");
    span.classList.add('loader');
    element.insertAdjacentElement('afterend',span);
    element.style.display = 'none';
    const uri = e.target.getAttribute('href');
    fetch(uri)
      .then(response => {
        return response.json();
      })
      .then(data => {
        console.log(data);
        span.remove();
        element.style.display = '';
        
        const para = document.querySelectorAll('p');
        para.forEach(el => {
          el.remove();
        });

        for (const key in data) {
          if (Object.hasOwnProperty.call(data, key)) {
            const value = (key == 'request') ? JSON.stringify(data[key]) : data[key];
            const para = document.createElement("p");
            const textNode = document.createTextNode(`${key}: ${value}`);
            para.appendChild(textNode);
            modal.insertAdjacentElement('beforeend', para);
          }
        }
        openModal();
      })
  });
});

