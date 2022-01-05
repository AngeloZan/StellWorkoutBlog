$(document).ready(function() {
    onHashChange();
    try {
        var initialHash = $('#initial-hash').text()
        window.location.hash = initialHash
    } catch {
        //pass
    }
    $('#mensagem_ajuda').trigger('autoresize'); 
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

M.textareaAutoResize = function ($textarea) {
    // Wrap if native element
    if ($textarea instanceof Element) {
      $textarea = $($textarea);
    }

    if (!$textarea.length) {
      console.error('No textarea element found');
      return;
    }

    // Textarea Auto Resize
    var hiddenDiv = $('.hiddendiv').first();
    if (!hiddenDiv.length) {
      hiddenDiv = $('<div class="hiddendiv common"></div>');
      $('body').append(hiddenDiv);
    }

    // Set font properties of hiddenDiv
    var fontFamily = $textarea.css('font-family');
    var fontSize = $textarea.css('font-size');
    var lineHeight = $textarea.css('line-height');
    var fontWeight = $textarea.css('font-weight');
    var letterSpacing = $textarea.css('letter-spacing');

    // Firefox can't handle padding shorthand.
    var paddingTop = $textarea.css('padding-top');
    var paddingRight = $textarea.css('padding-right');
    var paddingBottom = $textarea.css('padding-bottom');
    var paddingLeft = $textarea.css('padding-left');

    if (fontSize) {
      hiddenDiv.css('font-size', fontSize);
    }
    if (fontFamily) {
      hiddenDiv.css('font-family', fontFamily);
    }
    if (lineHeight) {
      hiddenDiv.css('line-height', lineHeight);
    }
    if (paddingTop) {
      hiddenDiv.css('padding-top', paddingTop);
    }
    if (paddingRight) {
      hiddenDiv.css('padding-right', paddingRight);
    }
    if (paddingBottom) {
      hiddenDiv.css('padding-bottom', paddingBottom);
    }
    if (paddingLeft) {
      hiddenDiv.css('padding-left', paddingLeft);
    }
    if (fontWeight) {
      hiddenDiv.css('font-weight', fontWeight);
    }
    if (letterSpacing) {
      hiddenDiv.css('letter-spacing', letterSpacing);
    }

    // Set original-height, if none
    if (!$textarea.data('original-height')) {
      $textarea.data('original-height', $textarea.height());
    }

    if ($textarea.attr('wrap') === 'off') {
      hiddenDiv.css('overflow-wrap', 'normal').css('white-space', 'pre');
    }

    hiddenDiv.text($textarea[0].value + '\n');
    var content = hiddenDiv.html().replace(/\n/g, '<br>');
    hiddenDiv.html(content);

    // When textarea is hidden, width goes crazy.
    // Approximate with half of window size

    if ($textarea[0].offsetWidth > 0 && $textarea[0].offsetHeight > 0) {
      hiddenDiv.css('width', $textarea.width() + 'px');
    } else {
      hiddenDiv.css('width', window.innerWidth / 2 + 'px');
    }

    /**
     * Resize if the new height is greater than the
     * original height of the textarea
     */
    if ($textarea.data('original-height') <= hiddenDiv.innerHeight()) {
      $textarea.css('height', hiddenDiv.innerHeight() + 'px');
    } else if ($textarea[0].value.length < $textarea.data('previous-length')) {
      /**
       * In case the new height is less than original height, it
       * means the textarea has less text than before
       * So we set the height to the original one
       */
      $textarea.css('height', $textarea.data('original-height') + 'px');
    }
    $textarea.data('previous-length', $textarea[0].value.length);
};

