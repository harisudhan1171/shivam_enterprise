    const track = document.getElementById('sliderTrack');
    const prevBtn = document.querySelector('.prev');
    const nextBtn = document.querySelector('.next');
    
    
    let index = 0;
    const slides = document.querySelectorAll('.slide');
    const slideWidth = slides[0].clientWidth;

    function updateSlider() {
        if(window.matchMedia('(max-width:600px)')){
            track.style.transform = `translateX(${-index * slideWidth}px)`;
        }
        else{
        track.style.transform = `translateX(${-index * slideWidth * 2}px)`;
        }
    }
    nextBtn.addEventListener('click', () => {
        
        if (index < slides.length -1) {
            index++;
            updateSlider();
        }
        else{
            index = 0;
            updateSlider();
        }
    });

    prevBtn.addEventListener('click', () => {
        if (index > 0) {
            index--;
            updateSlider();
        }
    });


    // window responsive
    window.addEventListener('resize', () => {
        updateSlider();
    });