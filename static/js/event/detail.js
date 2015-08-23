(function(){

    $(document).ready(function(){

        start_counter_select($('.counter-select'));

        $('#dt-check').change(function(){
            var places = $(this).find('option:selected').attr('places');
            $('#num-check').attr('max', places);
            $('#num-check').find('.delete').removeClass('active');
            $('#num-check').find('.add').addClass('active');
            $('#num-check').find('.num').val(1);
        });
    });


    // bar 位置固定
    $(function(){
        var rslidet = $("#planning").offset().top ;
        $(window).scroll(function() {
            if ($(document).scrollTop() > rslidet) {
                $("#planning-wrap").css({top: "0px", position: "fixed"});
            } else {
                $("#planning-wrap").removeAttr("style");
            }
        });
    });

    $(function(){
        var rslidet = $(".detail-order-box").offset().top ;
        $(window).scroll(function() {
            if ($(document).scrollTop() > rslidet) {
                $(".detail-order-box").css({top: "10px", position: "fixed"});
            } else {
                $(".detail-order-box").removeAttr("style");
            }
        });
    });





    // bar 模式切换
    $(function(){
        var q = [];
        var _cur = $("#planning-wrap a").size() - 1;
        for (i = 0; i <= _cur; i++) {
            q[i] = $('#q'+i).offset().top - 54;
            //eval("var q" + i + " = $('#q" + i + "').offset().top - 54;");
        }
        $("#planning-wrap a").click(function () {
            $('#planning-wrap a').removeClass('active');
            $(this).addClass("active");
            var index = $(this).index();
            $(window).scrollTop(q[index]);
        });


        $(window).scroll(function () {
            var s_top = $(window).scrollTop();
            var i = 0;
            var j = _cur;
            while (j > 0) {
                var tmp = q[j];
                //eval("var tmp = q" + j + ";");
                if (s_top < tmp - 1) {
                    j--;
                } else {
                    i = j;
                    break;
                }
            }
            $('#planning-wrap a').removeClass('active');
            $("#planning-wrap a").eq(i).addClass("active");
        });

    });


})();
