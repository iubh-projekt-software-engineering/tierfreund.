import Stepmation from './stepmation';
import toastr from 'toastr';
import Picker from 'pickerjs';

Array.from(document.querySelectorAll('.js--fullpicker')).forEach((el) => {
    const _picker = new Picker(el);
    console.log(_picker);
});

if (window.toastMessages) {
    window.toastMessages.forEach((message) => {
        toastr.info(message);
    });
}

if (document.querySelector('.onboarding--stage')) {
  const myStepmation = new Stepmation(document.querySelector('.onboarding--stage'));

  document.querySelector('.onboarding--stage_next').addEventListener('click', () => {
      myStepmation.next();
  });

  myStepmation.subscribe('in.before', (instance, container) => {
      container.style.display = 'block';
  });
  myStepmation.subscribe('out.after', (instance, container) => {
      if (instance.index < 1) {
          return;
      }
      instance.items[(instance.index - 1)].style.display = 'none';
      [].slice.call(document.querySelectorAll('.onboarding--stage_step')).forEach((el, index) => {
          if (instance.index === index) {
              el.classList.add('is--active');
          } else {
              el.classList.remove('is--active');
          }
      });
  });
  myStepmation.init();
}


Array.from(document.querySelectorAll('.js--password-toggler')).forEach((toggler) => {
  toggler.addEventListener('click', () => {
    const inputField = toggler.previousElementSibling;
    inputField.type = inputField.type === 'text' ? 'password' : 'text';
  });
});

const burger = document.querySelector('.burger');
const header = document.querySelector('.header');
const nav = document.querySelector('.navigation');

burger.addEventListener('click', () => {
    burger.classList.toggle('is--active');
    nav.classList.toggle('is--active');
    header.classList.toggle('is--active');  
});