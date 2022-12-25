$(function () {
// 提交表单数据到后台处理
    $('#textbutton').click(function () {
        var text = $('#query').val()
        $.ajax({
            type: 'get',
            data: {
                'text': text,
            },
            url: 'query',
            success: function (data) {
                // $('#emlist').
                console.log(typeof (data));
                console.log(data)

            }
        })
    });
    $('#username').change(function () {
        var name = $(this).val();
        // var csrf = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            type: "get",
            data: {
                'name': name,
            },
            url: "name",
            beforeSend: function () {
                // 禁用按钮防止重复提交，发送前响应
                $('#my_img').prop("hidden", false);
                $("#button").attr({disabled: "disabled"});
                // alert(1)
            },
            success: function (data) {
                console.log(data);
                // console.log(typeof (data));
                if (data != '1') {
                    $('#my_img').attr('src', '/static/img/prompt/gou.jpg')
                } else {
                    $('#my_img').attr('src', '/static/img/prompt/cha.gif')
                }
            },
            complete: function () {//完成响应
                // console.log(123)
                $("#button").removeAttr("disabled");
            },
        });
    });
    // $('#code').change(function () {
    //     var code = $(this).val();
    //     var csrf = $('input[name="csrfmiddlewaretoken"]').val();
    //     $.ajax({
    //         type: "post",
    //         data: {
    //             'code': code,
    //             'csrfmiddlewaretoken': csrf
    //         },
    //         // contentType: "application/json",
    //         url: "code",
    //         beforeSend: function () {
    //             // 禁用按钮防止重复提交，发送前响应
    //             $("#button").attr({disabled: "disabled"});
    //             alert(3)
    //         },
    //         success: function (data) {
    //             alert(data.status)
    //         },
    //         complete: function () {//完成响应
    //             $("#button").removeAttr("disabled");
    //             alert(4)
    //         },
    //     });
    // });
    $('#image').change(function () {
        console.log(this.files);
        var file = this.files[0];
        var url = window.URL.createObjectURL(file);
        $('#imgbd').attr('src', url)
    });
    $('#pwds').change(function () {
        var pwd = $('#pwd').val();
        var pwds = $('#pwds').val();
        // console.log(pwd, pwds)
        $.get('pwd', {
            'pwd': pwd,
            'pwds': pwds,
        }, function (data) {
            if (data == '1') {
            } else {
                alert('密码不匹配')
            }
        })
    });
    $('#button').click(function () {
        var username = $('#username').val();
        var name = $('#name').val();
        var pwd = $('#pwd').val();
        var code = $('#code').val();
        var sex = 0;
        $('.inputgri').each(function () {
            if ($(this).prop('checked') == true) {
                sex = $(this).val()
            }
        })
        $.post('regist', {
            'username': username,
            'name': name,
            'pwd': pwd,
            'code': code,
            'sex': sex,
        }, function (data) {

            window.location.href = '/login'
        })
    })
});
