(function() {

    var addImageToTextarea = function(id) {
        return function(url) {
            var textarea = $(id);
            var img = '<img src="' + url + '">';
            var text = textarea.val() + '\n' + img + '\n';
            textarea.val(text);
            textarea.scrollTop(textarea[0].scrollHeight);

        };
    };



    $(document).ready(function(){
        $("#event-images").uploader({
            maxLength: 12,
            name:'covers',
            width:'80px',
            height:'80px'
        });

        $("#planning-image").uploader({
            maxLength: 1,
            width:'80px',
            height:'80px',
            success: addImageToTextarea('#planning'),
        });

        $("#fee-desc-image").uploader({
            maxLength: 1,
            width:'80px',
            height:'80px',
            success: addImageToTextarea('#fee-desc'),
        });

        $("#equipment-image").uploader({
            maxLength: 1,
            width:'80px',
            height:'80px',
            success: addImageToTextarea('#equipment'),
        });


        $("#event-form").validate({
            rules: {
                title: "required",
                outline: "required",
                route: "required",
                type_id: "required",
                intensity: "required",
                days: {
                    required: true,
                    digits: true,
                },
                places: {
                    required: true,
                    digits: true,
                },
                price: {
                    required: true,
                    number: true,
                },
                planning: "required",
                'fee-desc': "required",
                equipment: "required",

            },

            submitHandler: function(form) {
                if ($('#event-images input').length == 0) {
                    alert('请添加图片');
                }
                var data = $(form).serialize();
                var method = $(form).attr('method');
                var action = $(form).attr('action');
                $.ajax({
                    type: method,
                    url: action,
                    data: data,
                    dataType: 'json',
                    success: function (data, textStatus) {
                        if (data.code) {
                            alert(data.msg);
                        }
                        location.href = "/admin/events/";
                    },
                    error: function (XMLHttpRequest, textStatus, errorThrown) {
                        alert('提交失败');
                    },
                });

            },

        });


        $("#event-images").uploader('setValues', coversInit);

    });

})();
