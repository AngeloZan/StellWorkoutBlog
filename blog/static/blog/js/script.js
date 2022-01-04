$(document).ready(function(){
    $(".owl-carousel").owlCarousel();

    $(document).on('mouseenter.hover-reveal','.hover-reveal', function (e){
        $(this).find('.card-reveal').css({ overflowY: 'hidden', height: '60%', transform: 'translateY(-100%)', paddingTop: "0px", paddingBottom: "5px" });
        $(this).find('.card-reveal').stop().fadeIn(300);
    });
  
    $(document).on('mouseleave.hover-reveal','.hover-reveal', function (e){
        $(this).find('.card-reveal').stop().fadeOut(150);
    });

    var favouriteClicked = false;

    $('.favourite-button').on('mousedown', function() {
        favouriteClicked = true;
    });

    $(window).on('mouseup', function() {
        favouriteClicked = false;
    });

    $('.post-card').each(function() {
        this.addEventListener('mousedown', () => {
            this.addEventListener('mousemove', flagged);
        });
        this.addEventListener('mouseup', (e) => {
            if (! this.isScrolled) {
                if (! favouriteClicked) {
                    var link = $(this).find('.card-title').find('.post-link').attr('href');
                    var domain = window.location.protocol + '//' + window.location.host;
                    var win = window.open(`${domain}${link}`)
                    if (win) {
                        window.focus()
                    } 
                } 
            }
            this.isScrolled = false;
            this.removeEventListener('mousemove', flagged)
        })
    });
});

function isOverflown(element) {
    return element.scrollHeight > element.clientHeight || element.scrollWidth > element.clientWidth;
}

$('.favourite-button').on('click', function() {
    var id = $(this).find('.post-id').text();
    var elements = document.querySelectorAll(`#favourite_button_${id}`)
   
    for (var element of elements) {
        $(element).find('.material-icons').toggleClass('saved');
        element.animate([
            { transform: 'translateY(-6px)' },
            { transform: 'translateY(0px)' }
        ], {
            duration: 150,
            iterations: 1
        });
    }
    var domain = window.location.protocol + '//' + window.location.host;
    $.ajax({
        type: 'GET',
        url: `${domain}/${id}/favourite-post/`
    });
});

function flagged () {
    this.isScrolled = true;
};


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
        728:{
            margin:20,
            items:6,
        },
        1000:{
            items:6,
            margin:20
        },
        1200:{
            mergeFit:false,
            items:8
        }
    }
})




  
         

