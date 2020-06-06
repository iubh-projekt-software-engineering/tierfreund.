import Stepmation from './stepmation';

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