(function(){


    $(document).ready(function(){
        $('.auto-approve').change(function(){
            var sid = $(this).attr('sid');
            var val = this.checked ? 1 : 0;

            $.ajax({
                type: 'GET',
                url: '/admin/sessions/autoapprove/',
                data: {sid: sid, auto: val},
                dataType: 'json',
                success: function(data) {
                    window.location.reload();
                },
                error: function(data) {
                    alert('更改失败');
                },

            });

        });


    });

})();
