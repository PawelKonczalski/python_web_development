$(document).ready(function () {
    $(document).on('submit', '#register-form', function (e) {
        e.preventDefault();
        let form = $('#register-form').serialize();
        $.ajax({
            url: '/registration',
            type: 'POST',
            data: form,
            success: function (response) {
                console.log(response)
            }
        })
    });

    $(document).on('submit', '#login-form', function (e) {
        e.preventDefault();
        let form = $(this).serialize();
        $.ajax({
            url: '/check-login',
            type: 'POST',
            data: form,
            success: function (res) {
                if (res === 'error') {
                    alert('Could not log in');
                } else {
                    window.location.href = '/'

                }
            }
        })
    });

    $(document).on('click', '#logout-link', function (e) {
        e.preventDefault();
        $.ajax({
            url: '/logout',
            type: 'GET',
            success: function (res) {
                if (res === 'success') {
                    window.location.href = '/'
                } else {
                    alert('Something went wrong')
                }
            }
        })
    });

    $(document).on('submit', '#post-activity', function (e) {
        form = $(this).serialize();
        $.ajax({
            url: '/post-activity',
            type: 'POST',
            data: form,
            success: function (res) {
                if (res === 'success') {
                    console.log(res);
                }
            }
        })
    })
});