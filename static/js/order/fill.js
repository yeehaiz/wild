(function(){
    var persondict = {}
    for (var i=0 ; i < persons.length; i++){
        persondict[persons[i].id] = persons[i];
    }

    var set_person_form = function(form, data) {
        form.find('input[name^="person_name_"]').val(data.name);
        form.find('input[name^="person_phone_"]').val(data.mobile);
        form.find('input[name^="credentials_type_"]').val(data.cert_type);
        form.find('input[name^="credentials_no_"]').val(data.cert);
        form.find('input[name^="person_sex_"][value="'+ data.sex +'"]')[0].checked = true;
        form.find('input[name^="person_birthday_"]').val(data.birthday);
    };

    var fill_person = function(pid) {
        var forms = $('.pasger-list .pasger-form');
        for (var i =0; i<forms.length; i++){
            var form = $(forms[i]);
            if (!form.attr('p_no') && ! form.find('#qt_name_'+(i+1)).val().trim()){
                var person = persondict[pid];
                set_person_form(form, person);
                form.attr('p_no', pid);
                return true;
            }
        }
        return false;
    };
    var unfill_person = function(pid) {
        var forms = $('.pasger-list .pasger-form[p_no="'+pid +'"]');
        if (forms.length) {
            set_person_form(forms, {
                'name': '',
                'mobile': '',
                'cert_type': 1,
                'cert': '',
                'sex': 'm',
                'birthday': '',
            });
            forms.removeAttr('p_no');
            return true;
        }
        return true;
    };

    $(document).ready(function(){
        $('.datepicker').datepicker();

        $('.contact-list .item-check').click(function(){
            var checkbox = $(this).find('.input-checkbox')[0];
            var pid = checkbox.id.substring(7);
            if (checkbox.checked == false) {
                r = fill_person(pid);
                if (r) checkbox.checked = true;
            } else {
                r = unfill_person(pid);
                if (r) checkbox.checked = false;
            }
            return false;
        });

        $('.pasger-actions .clear-input').click(function(){
            var form = $(this).parent().parent().find('.pasger-form');
            var pid = form.attr('p_no');
            if (pid) {
                r = unfill_person(pid);
                if (r) {
                    $('.contact-list #person_'+pid)[0].checked = false;
                }
            } else {
                set_person_form(form, {
                    'name': '',
                    'mobile': '',
                    'cert_type': 1,
                    'cert': '',
                    'sex': 'm',
                    'birthday': '',
                });
            }
        });

    });

})();
