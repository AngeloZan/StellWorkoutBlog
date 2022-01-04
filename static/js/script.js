$(document).ready(function() {
    $('select').formSelect();

    // dark theme stuff
    const toggleSwitch = document.querySelector('.theme-switch input[type="checkbox"]');
    var logo_branca = document.querySelector('#white-logo-a');
    var logo_preta = document.querySelector('#black-logo-a');
    var account_branco = document.querySelectorAll('#profile-white')
    var account_preto = document.querySelectorAll('#profile-black')

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
                for (var i=0; i<account_preto.length; i++) {
                    account_branco[i].style.display = logo_branca.style.display;
                    account_preto[i].style.display = 'none';
                };
            } else {
                for (element of document.querySelectorAll('.theme-switch input[type="checkbox"]')) {
                    element.checked = false;
                };
                document.documentElement.setAttribute('data-theme', 'light');
                logo_preta.style.display = logo_branca.style.display;
                logo_branca.style.display = 'none';
                for (var i=0; i<account_preto.length; i++) {
                    account_preto[i].style.display = logo_preta.style.display;
                    account_branco[i].style.display = 'none';
                };
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
        if (($(this).prop('href') == window.location.href) && (! ($(this).attr('href') == '#'))) {
            $(this).addClass('highlight-link');
        }
    });

    $('.bookmark-icon.highlight-link').each(function() {
        $(this).find('i').text('bookmark')
    });

    $('.modal').modal();
});








