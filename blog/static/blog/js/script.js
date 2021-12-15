$(document).ready(function(){
    $(".owl-carousel").owlCarousel();
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




  
         

