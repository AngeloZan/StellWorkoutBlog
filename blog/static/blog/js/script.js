$(document).ready(function(){
    $(".owl-carousel").owlCarousel();

    $(document).on('mouseenter.hover-reveal','.hover-reveal', function (e){
        $(this).find('.card-reveal').css({ height: '60%', transform: 'translateY(-100%)', paddingTop: "0px", paddingBottom: "5px" });
        $(this).find('.card-reveal').fadeIn(250);
    });
  
    $(document).on('mouseleave.hover-reveal','.hover-reveal', function (e){
        $(this).find('.card-reveal').fadeOut(250);
    });

    var favouriteClicked = false;

    $('.favourite-button').on('click', function() {
        favouriteClicked = true;
    });

    $('.post-card').on('click', function() {
        if (! favouriteClicked) {
            var link = $(this).find('.card-title').find('.post-link').attr('href');
            var domain = window.location.protocol + '//' + window.location.host;
            var win = window.open(`${domain}${link}`)
            if (win) {
                window.focus()
            } else {
                alert('Por favor permita popups neste site.')
            }
        } 
    });
});

$('.owl-carousel').owlCarousel({
    items:8,
    loop:false,
    nav:false,
    merge:true,
    margin:30,
    transitionStyle: "fade",
    animateIn:'fadeIn',
    animateOut:'fadeOut',
    responsiveClass:true,
    responsive:{
        0:{
            margin:15,
            items:4,
        },
        600:{
            margin:20,
            items:6,
        },
        1000:{
            items:8,
            mergeFit:false
        }
    }
})




  
         

