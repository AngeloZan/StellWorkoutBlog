$(document).ready(function() {
    onHashChange();
    try {
        var initialHash = $('#initial-hash').text()
        window.location.hash = initialHash
    } catch {
        //pass
    }
});

window.addEventListener('hashchange', onHashChange)

function onHashChange() {
    var hash = window.location.hash;
    try {
        var id = hash.slice(1);
        var allowedIds = ['editar-perfil', 'notificacoes', 'alterar-senha', 'ajuda', 'modal-sair'];
        if (! allowedIds.includes(id)) {
            id = 'editar-perfil';
        };
        $('.profile-forms-container .row').removeClass('active');
        $(`#${id}`).addClass('active');
        $('.profile-sidenav li').removeClass('active');
        $(`#${id}-trigger`).parent('li').css({ borderRight: 'none' })
        $(`#${id}-trigger`).parent('li').addClass('active');
        if (id == 'alterar-senha') {
            $('#id_old_password').focus();
        };
    } catch {
        //pass
    }
}

$('.profile-sidenav li>a').hover(function() {
    if ((! $(this).parent('li').hasClass('active')) && (! ($(this).parent('li').attr('id') == 'sair')) ) {
        $(this).parent('li').css({ borderRight: 'solid 3px #A2A2A2' });
    }
    
}, function() {
    if ($(this).parent('li').css('border-right') == '3px solid rgb(162, 162, 162)') {
        $(this).parent('li').css({ borderRight: 'none' });
    }
});

$('.cb-notificacoes').on('change', function() {
    var form = $('#notificacoes-form');
    var url = form.attr('action');
    $.ajax({
        type: "POST",
        url: url,
        data: form.serialize()
    });
});

