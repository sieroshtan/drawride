$(document).ready(function () {
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            function getCookie(name) {
                var cookieValue = null;
                if (document.cookie && document.cookie != '') {
                    var cookies = document.cookie.split(';');
                    for (var i = 0; i < cookies.length; i++) {
                        var cookie = jQuery.trim(cookies[i]);
                        if (cookie.substring(0, name.length + 1) == (name + '=')) {
                            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                            break;
                        }
                    }
                }
                return cookieValue;
            }
            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });

    $('.show-lightbox').on('click', function(event) {
        event.preventDefault();
        $('#overlay').fadeIn('fast');
    });

    $(document).on('click', '#close-lightbox, #overlay-bg', function(event) {
        event.preventDefault();
        $('#overlay').fadeOut('fast');
    });

    $('#compose-message').click(function (event) {
        event.preventDefault();
        var a = $(this).attr('href');
        $('#overlay').fadeIn('fast');
        $('#lightbox').load(a);
    });

    $('#overlay').on('submit', '#form-compose', function (event) {
        event.preventDefault();
        var form = $(this);

        $.ajax({
            type: 'POST',
            data: form.serialize(),
            url: form.attr('action'),
            success: function (data) {
                form.find('#id_text').val('');
                $('#lightbox').html(data)
                $('#overlay').fadeOut('fast');
            }
        });
    });

    $('.follow,.unfollow').on('click', function(event) {
        event.preventDefault();
        var a = $(this);
        $.ajax({
            type: 'POST',
            url: a.attr('href'),
            success: function (result) {
                $('.hidden').removeClass('hidden');
                $(a).addClass('hidden');
                var following_count = parseInt($('.followers .count').text());

                if (a.attr('href').indexOf('unfollow') != -1) {
                    following_count -= 1;
                } else {
                    following_count += 1;
                }
                $('.followers .count').text(following_count);
            }
        });
    });

    $('#form-post-comment').submit(function (event) {
        event.preventDefault();
        var form = $(this);

        if (form.find('#id_text').val().trim() == '') {
            alert('Please enter a comment before sending.')
        }

        $.ajax({
            type: 'POST',
            data: $(this).serialize(),
            url: form.attr('action'),
            success: function (result) {
                $('#comments').html(result);
                form.find('#id_text').val('').focus();
            }
        });
    });

    $('.join').on('click', function(event) {
        event.preventDefault();
        var a = $(this);

        $.ajax({
            type: 'POST',
            url: a.attr('href'),
            success: function (result) {
                $('.join.hidden').removeClass('hidden');
                $(a).addClass('hidden');
                $('#members-list').html(result.members);
            }
        });
    });

    $('.favorite').on('click', function(event) {
        event.preventDefault();
        var a = $(this);

        $.ajax({
            type: 'POST',
            url: a.attr('href'),
            success: function (result) {
                $('.favorite.hidden').removeClass('hidden');
                $(a).addClass('hidden');
            }
        });
    });

    $('.close').on('click', function() {
        $('#notices').slideUp('fast');
    });
});
