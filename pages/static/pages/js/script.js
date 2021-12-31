$(document).ready(function(){
    $(".owl-carousel").owlCarousel();

    var timeOuts = [];

    $(document).on('mouseenter.title','.title', function (e){
        $(this).parent().find('p').css({ visibility: 'visible', opacity: '1' });
        $(this).css({ color: 'white' });
        for (var i=0; i<timeOuts.length; i++) {
            clearTimeout(timeOuts[i]);
        }
    });

    $(document).on('mouseleave.txt','.txt', function (e){
        timeOuts.push(setTimeout(() => {
            $(this).find('p').css({ opacity: '0' });
            $(this).find('.title').css({ color: 'rgba(255, 255, 255, 0.2)' });
        }, 1200));
    });

    
    var titles = document.querySelectorAll('.txt .title')

});


var owl = $('.owl-carousel');

owl.owlCarousel({
    items:1,
    loop:false,
    nav:false,
    merge:false,
    margin:0,
    mouseDrag:false,
    transitionStyle: "fade",
    animateIn:'fadeIn',
    animateOut:'fadeOut',
    responsiveClass:false,
    autoplay:true,
    autoplayTimeout:3000,
    autoplayHoverPause:false,
});

owl.on('mousewheel', '.owl-stage', function (e) {
    if (e.originalEvent.deltaY>0) {
        owl.trigger('next.owl');
    } else {
        owl.trigger('prev.owl');
    }
    e.preventDefault();
});

owl.on('changed.owl.carousel', function(event) {
    owl.trigger('stop.owl.autoplay');
    toggleTheme();
});

function toggleTheme() {
    var logo_branca = document.querySelector('#white-logo-a');
    var logo_preta = document.querySelector('#black-logo-a');

    if (logo_preta.style.display != "none") {
        document.documentElement.setAttribute('data-theme', 'dark');
        logo_branca.style.display = logo_preta.style.display;
        logo_preta.style.display = 'none';
    } else {
        document.documentElement.setAttribute('data-theme', 'light');
        logo_preta.style.display = logo_branca.style.display;
        logo_branca.style.display = 'none';
    }
}



