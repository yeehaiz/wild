(function() {

    var set_error = function(msg) {
        if (msg === null) {
            $('#register-error-container').html('');
            return;
        }

        var inner = '<div class="register-error alert alert-danger alert-dismissible" role="alert">' +
                '<button type="button" class="close" data-dismiss="alert" aria-label="Close">' +
                '<span aria-hidden="true">&times;</span>' +
                '</button>' +
                '<span>' + msg + '</span>' +
                '</div>';

        $('#register-error-container').html(inner);
    };

    var send_verify_code_timeout = function(seconds) {
        if (seconds > 0) {
            var text = '重新发送' + '(' + seconds + ')';
            $('#btn-vcode').text(text);
            $('#btn-vcode').addClass('disabled');
            setTimeout(function() {send_verify_code_timeout(seconds-1);}, 1000);
        } else {
            var text = '获取验证码';
            $('#btn-vcode').text(text);
            $('#btn-vcode').removeClass('disabled');
        }
    };



    var check_username = function() {
        var username = $('#username').val().trim();
        $.ajax({
            type: 'GET',
            url: '/user/register/check_username/',
            data: {username: username},
            dataType: 'json',
            success: function (data, textStatus) {
                if (data.code) {
                    set_error(data.msg);
                    $('#username-ok').addClass('hide');
                    $('#username-remove').removeClass('hide');
                } else {
                    set_error(null);
                    $('#username-ok').removeClass('hide');
                    $('#username-remove').addClass('hide');
                }
            },
        });

    };

    var send_verify_code = function() {
        var mobile = $('#mobile').val().trim();
        $.ajax({
            type: 'POST',
            url: '/user/verifycode/',
            data: {mobile: mobile},
            dataType: 'json',
            success: function (data, textStatus) {
                if (data.code) {
                    set_error(data.msg);
                } else {
                    send_verify_code_timeout(60);
                }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                set_error('获取验证码失败');
            },
        });
    };

    var register = function() {
        var form_data = $('#register-form').serialize();
        $.ajax({
            type: 'POST',
            url: '/user/register/post/',
            data: form_data,
            dataType: 'json',
            success: function (data, textStatus) {
                if (data.code) {
                    set_error(data.msg);
                } else {
                    location.href = $('#redirectURL').val();
                }
            },
            error: function (XMLHttpRequest, textStatus, errorThrown) {
                set_error('注册失败');
            },
        });
    };



    $(document).ready(function(){

        $('#username').blur(check_username);
        $('#btn-vcode').click(send_verify_code);
        $('#submit').click(register);

    });




})();
