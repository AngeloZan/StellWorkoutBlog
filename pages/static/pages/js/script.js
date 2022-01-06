$(document).ready(function(){
    $(".owl-carousel").owlCarousel();

    var timeOuts = [];

    $(document).on('mouseenter.title','.title', function (e){
        $(this).parent().find('p').css({ visibility: 'visible', opacity: '1' });
        $(this).css({ color: 'white' });
        for (var i=0; i<timeOuts.length; i++) {
            if (timeOuts[i][1] == $(this).parent().attr('id')) {
                clearTimeout(timeOuts[i][0]);
            };
        }
    });

    $(document).on('mouseleave.txt','.txt', function (e){
        timeOuts.push([setTimeout(() => {
            $(this).find('p').css({ opacity: '0' });
            $(this).find('.title').css({ color: 'rgba(255, 255, 255, 0.2)' });
        }, 1200), $(this).attr('id')]);
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
    touchDrag:false,
    transitionStyle: "fade",
    animateIn:'fadeIn',
    animateOut:'fadeOut',
    responsiveClass:false,
    autoplay:true,
    autoplayTimeout:3000,
    autoplayHoverPause:false,
    onTranslate: toggleTheme,
});

var waitTxts = true;

function toggleTheme() {
    var logo_branca = document.querySelector('#white-logo-a');
    var logo_preta = document.querySelector('#black-logo-a');

    if (document.documentElement.getAttribute('data-theme') != 'dark') {
        document.documentElement.setAttribute('data-theme', 'dark');
        logo_branca.style.display = logo_preta.style.display;
        logo_preta.style.display = 'none';
        $('.page-footer').css({ width: '100vw', position: 'absolute', top: '100%', left: '0px', margin: '0' });
        if (waitTxts) {
            waitTxts = false;
            setTimeout(() => {
                $('#left-txt').css({ opacity: '1' })
            }, 1500);
            setTimeout(() => {
                $('#right-txt').css({ opacity: '1' })
            }, 1800);
        };
    } else {
        console.log('else')
        document.documentElement.setAttribute('data-theme', 'light');
        logo_preta.style.display = logo_branca.style.display;
        logo_branca.style.display = 'none';
    }
    owl.trigger('stop.owl.autoplay');
}






