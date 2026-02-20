document.addEventListener('DOMContentLoaded', function() {

    const humburger = document.querySelector(".humburger");
    const navlinks = document.querySelector(".nav-links");

    humburger.addEventListener("click", () => {
        humburger.classList.toggle("active");
        navlinks.classList.toggle("active");
    });

    const skillsSection = document.querySelector('.skills-section');
    const skillsBars = document.querySelectorAll('.skill-bar');
    const percentNumber = document.querySelectorAll('.percent-number');

    let skillAnimted = false;

    function animateSkills() {
        if (skillAnimted) return;
        skillAnimted = true;

        skillsBars.forEach((bar, index) => {
            const progress = bar.querySelector('.skill-progress');
            const percent = parseInt(progress.getAttribute('data-percent'));
            
            progress.style.width = percent + '%';

            let currentPercent = 0;
            const updateCounter = setInterval(() => {
                if (currentPercent < percent) {
                    currentPercent++;
                    percentNumber[index].textContent = currentPercent;
                } else {
                    clearInterval(updateCounter);
                }
            }, 20);
        });
    }

    const statsSection = document.querySelector('.stats-section');
    const counters = document.querySelectorAll('.stat-number');

    let statAnimated = false;

    function animatestate() {
        if (statAnimated) return;
        statAnimated = true;

        counters.forEach(counter => {
            const target = +counter.getAttribute('data-target');
            const duration = 2000; 
            const increament = target / (duration / 16); 

            let currentCount = 0;

            const updateCount = () => {
                if (currentCount < target) {
                    currentCount += increament;
                    counter.textContent = Math.floor(Math.min(currentCount, target));
                    requestAnimationFrame(updateCount);
                } else {
                    counter.textContent = target;
                }
            };
            
            updateCount();
        });
    }

    const observerOption = {
        root: null,
        rootMargin: '0px',
        threshold: 0.5
    };

    const skillsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animateSkills();
                skillsObserver.unobserve(entry.target);
            }
        });
    }, observerOption);

    if (skillsSection) {
        skillsObserver.observe(skillsSection);
    }

    const statsObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                animatestate();
                statsObserver.unobserve(entry.target);
            }
        });
    }, observerOption);

    if (statsSection) {
        statsObserver.observe(statsSection);
    }

    AOS.init();
});

