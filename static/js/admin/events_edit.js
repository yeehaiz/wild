(function() {


    var addImageToTextarea = function(id) {
        return function(url) {
            var textarea = $(id);
            var img = '<img src="' + url + '">';
            var text = textarea.val() + '\n' + img + '\n';
            textarea.val(text);
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

    });

})();
