$(document).ready(function(e) {
    $('select').formSelect();

    // dark theme stuff
    var toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
    var logo_branca = document.querySelector('#white-logo-a');
    var logo_preta = document.querySelector('#black-logo-a');

    $('.theme-switch input[type="checkbox"]').each(function() {
        var checkbox = this;
        checkbox.addEventListener('change', function(e) {
            if (e.target.checked) {
                for (element of document.querySelectorAll('.theme-switch input[type="checkbox"]')) {
                    element.checked = true;
                };
                document.documentElement.setAttribute('data-theme', 'dark');
                logo_branca.style.display = logo_preta.style.display;
                logo_preta.style.display = 'none';
                // mostrar lua
                $('.toggle-theme-link').find('i').removeClass('my-custom-icons-sun');
                $('.toggle-theme-link').find('i').addClass('my-custom-icons-moon');

            } else {
                for (element of document.querySelectorAll('.theme-switch input[type="checkbox"]')) {
                    element.checked = false;
                };
                document.documentElement.setAttribute('data-theme', 'light');
                logo_preta.style.display = logo_branca.style.display;
                logo_branca.style.display = 'none';
                // mostrar sol
                $('.toggle-theme-link').find('i').removeClass('my-custom-icons-moon');
                $('.toggle-theme-link').find('i').addClass('my-custom-icons-sun');
            }
            $.ajax({
                type: 'GET',
                url: `${window.location.protocol + '//' + window.location.host}/toggle-theme/`
            });
        });
    });

    $('.bookmark-icon').on('mouseenter', function() {
        $(this).find('i').text('bookmark')
    });

    $('.bookmark-icon').on('mouseleave', function() {
        if (! ($(this).prop('href') == window.location.href)) {
            $(this).find('i').text('bookmark_border')
        }
    });

    //highlight current page link on navbar
    $('nav a').each(function(){
        if (($(this).prop('href') == window.location.href) && (! ($(this).attr('href') == '#')) && (! ($(this).attr('href') == '#!'))) {
            $(this).addClass('highlight-link');
        }
    });

    $('.bookmark-icon.highlight-link').each(function() {
        $(this).find('i').text('bookmark')
    });

    $('.modal').modal();

    //navbar stuff
    var inMobile = false;
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
    $("nav .dropdown-trigger").dropdown({
        coverTrigger: false,
        alignment: 'right'
    });

    $("#search-icon").click(function(e) {

        if($("#menu-icon").is(":visible")) {
            inMobile = true;
        } else {
            inMobile = false;
        }

        $("#search-icon").hide();
        var activeLogo = $('.logo-nav:visible');
        activeLogo.addClass('previous-active-logo');
        activeLogo.hide();
        if(inMobile) {
            $("#menu-icon").css("display", "none");
        } else {
            $("#comp-menu").hide();
        }
        $("#search-div").fadeIn();
        $("#search-txt").focus();
    });

    $("#close-icon").click(function(e) {
        $("#search-div").hide();
        $("#search-icon").fadeIn();
        var previousActiveLogo = $(".previous-active-logo").first();
        previousActiveLogo.fadeIn();
        previousActiveLogo.removeClass('previous-active-logo');
        if(inMobile) {
            $("#menu-icon").css("display", "unset");
        } else {
            $("#comp-menu").fadeIn();
        }
    });

    $("#search-txt").blur(function(e) {
        $("#search-div").hide();
        $("#search-icon").fadeIn();
        var previousActiveLogo = $(".previous-active-logo").first();
        previousActiveLogo.fadeIn();
        previousActiveLogo.removeClass('previous-active-logo');
        if(inMobile) {
            $("#menu-icon").fadeIn();
        } else {
            $("#comp-menu").fadeIn();
        }
    })
});

$('.toggle-theme-link').click(function(e) {
    $('.theme-switch input[type="checkbox"]').first().click();
});









