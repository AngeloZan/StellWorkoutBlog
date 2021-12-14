$(document).ready(function(){
    $(".owl-carousel").owlCarousel();
});

$('.owl-carousel').owlCarousel({
    items:8,
    loop:false,
    merge:true,
    margin:30,
    responsiveClass:true,
    responsive:{
        0:{
            margin:15,
            items:4,
            nav:true
        },
        600:{
            margin:20,
            items:6,
            nav:true
        },
        1000:{
            items:8,
            nav:true,
            mergeFit:false
        }
    }
})



  
         

