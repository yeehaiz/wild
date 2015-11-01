(function(){

    var ORDER_STATUSES = {
        1: '未审核',
        2: '预审通过',
        3: '已通过',
        4: '报名成功',
        5: '替补',
    };


    $(document).ready(function(){
        $('.status-setting').change(function(){
            var oid = $(this).attr('oid');
            var val = $(this).val();
            var sure = confirm('确定将审核状态改成"' + ORDER_STATUSES[val] + '"吗？');
            if (sure) {
                $.ajax({
                    type: 'GET',
                    url: '/admin/sessions/orders/status/',
                    data: {oid: oid, status: val},
                    dataType: 'json',
                    success: function(data) {
                        window.location.reload();
                    },
                    error: function(data) {
                        alert('更改失败');
                    },

                });
            }
        });


    });

})();
