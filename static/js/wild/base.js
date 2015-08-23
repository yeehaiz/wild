(function() {

    var _get_val = function(parent) {
        var val = parseInt(parent.find('.num').val());
        return isNaN(val) ? 0 : val;
    };

    var _update = function(parent, value) {
        var max = Infinity;
        var min = -Infinity;

        var val = _get_val(parent);

        if (parent.attr('min') !== undefined) min = parseInt(parent.attr('min'));
        if (parent.attr('max') !== undefined) max = parseInt(parent.attr('max'));


        // minus
        if (val > value) {
            if (value >= min) {
                parent.find('.num').val(value);
            }
            if (value <= min) {
                parent.find('.delete').removeClass('active');
            }
            if (value < max) {
                parent.find('.add').addClass('active');
            }
        }

        // add
        if (val < value) {
            if (value <= max){
                parent.find('.num').val(value);
            }
            if (value >= max){
                parent.find('.add').removeClass('active');
            }
            if (value > min) {
                parent.find('.delete').addClass('active');
            }
        }

    };


    var _counter_select_events = function(jsel, callback) {

        jsel.find('> .delete').click(function(){
            var parent = $(this).parent();
            _update(parent, _get_val(parent) -1);
            if (callback != undefined) {
                callback(parent);
            }
        });


        jsel.find('> .add').click(function(){
            var parent = $(this).parent();
            _update(parent, _get_val(parent) +1);
            if (callback != undefined) {
                callback(parent);
            }
        });

    };


    this.start_counter_select = _counter_select_events;

})();
