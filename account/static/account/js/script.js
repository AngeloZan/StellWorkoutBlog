$('.profile-sidenav li a').on('click', function() {
    $('.profile-sidenav li').removeClass('active');
    $(this).parent('li').addClass('active');
    $('.profile-forms-container .row').removeClass('active');
    var idLink = $(this).attr('id');
    var id = idLink.substring(0, idLink.lastIndexOf("-"));
    console.log(id);
    $(`#${id}`).addClass('active');
});

