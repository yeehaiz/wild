(function(){

    $(document).ready(function(){

        $('#dt-check').change(function(){
            var places = $(this).find('option:selected').attr('places');
            $('#num-check').attr('max', places);
            $('#num-check').find('.delete').removeClass('active');
            $('#num-check').find('.add').addClass('active');
            $('#num-check').find('.num').val(1);
        });
    });


})();
