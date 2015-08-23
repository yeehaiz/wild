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

    var checkMobile = function (value) {
        if (!(/^1[3|4|5|7|8][0-9]\d{8}$/.test(value))) {
            return false;
        }
        return true;
    };

    var checkIdcardOrder = function (value, element, sexE, birthdayE) {
        value = value.trim();
        $(element).val(value);
        /*
         var idLength = value.length;
         if(idLength != 15 && idLength != 18){
         return false;
         }
         for(i = 0; i < idLength; i++){
         var nm = value.charAt(i);
         if((nm < 0 || nm > 9) && idLength != 17 && idLength != 15){
         return false;
         }
         if(idLength == 17 && ((nm != 'X' && nm != 'x') && isNaN(nm) )){
         return false;
         }
         }
         return true;
         */
        var area = {11: "北京", 12: "天津", 13: "河北", 14: "山西", 15: "内蒙古", 21: "辽宁", 22: "吉林", 23: "黑龙江", 31: "上海", 32: "江苏", 33: "浙江", 34: "安徽", 35: "福建", 36: "江西", 37: "山东", 41: "河南", 42: "湖北", 43: "湖南", 44: "广东", 45: "广西", 46: "海南", 50: "重庆", 51: "四川", 52: "贵州", 53: "云南", 54: "西藏", 61: "陕西", 62: "甘肃", 63: "青海", 64: "宁夏", 65: "xinjiang", 71: "台湾", 81: "香港", 82: "澳门", 91: "国外"};
        var idcard = value;
        var Y, JYM;
        var S, M;
        var sex_val;
        var idcard_array = new Array();
        idcard_array = idcard.split("");
        if (area[parseInt(idcard.substr(0, 2))] == null) {
            return false;
        }
        switch (idcard.length) {
        case 15:
            if ((parseInt(idcard.substr(6, 2)) + 1900) % 4 == 0 || ((parseInt(idcard.substr(6, 2)) + 1900) % 100 == 0 && (parseInt(idcard.substr(6, 2)) + 1900) % 4 == 0)) {
                ereg = /^[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}$/;
            } else {
                ereg = /^[1-9][0-9]{5}[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}$/;
            }
            if (ereg.test(idcard)) {
                if (parseInt(idcard_array[14]) % 2 == 0) {
                    sex_val = 'f';
                } else {
                    sex_val = 'm';
                }
                if (sexE) {
                    //sexE.find('#sex_select').text(sex_val);
                    sexE.find('input[name^=person_sex]').each(function(){
                        if($(this).val()==sex_val){
                            //$(this).attr('checked','checked');
                            this.checked = true;
                            return false;
                        }
                    });
                }
                birthdayE && birthdayE.val('19' + idcard.substr(6, 2) + '-' + idcard.substr(8, 2) + '-' + idcard.substr(10, 2));
                birthdayE && birthdayE.parent().find('div.input-tips').remove();
                return true;
            } else {
                return false;
            }
            break;
        case 18:
            if (parseInt(idcard.substr(6, 4)) % 4 == 0 || (parseInt(idcard.substr(6, 4)) % 100 == 0 && parseInt(idcard.substr(6, 4)) % 4 == 0)) {
                ereg = /^[1-9][0-9]{5}(19|20)[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|[1-2][0-9]))[0-9]{3}[0-9Xx]$/;
            } else {
                ereg = /^[1-9][0-9]{5}(19|20)[0-9]{2}((01|03|05|07|08|10|12)(0[1-9]|[1-2][0-9]|3[0-1])|(04|06|09|11)(0[1-9]|[1-2][0-9]|30)|02(0[1-9]|1[0-9]|2[0-8]))[0-9]{3}[0-9Xx]$/;
            }
            if (ereg.test(idcard)) {
                S = (parseInt(idcard_array[0]) + parseInt(idcard_array[10])) * 7 + (parseInt(idcard_array[1]) + parseInt(idcard_array[11])) * 9 + (parseInt(idcard_array[2]) + parseInt(idcard_array[12])) * 10 + (parseInt(idcard_array[3]) + parseInt(idcard_array[13])) * 5 + (parseInt(idcard_array[4]) + parseInt(idcard_array[14])) * 8 + (parseInt(idcard_array[5]) + parseInt(idcard_array[15])) * 4 + (parseInt(idcard_array[6]) + parseInt(idcard_array[16])) * 2 + parseInt(idcard_array[7]) * 1 + parseInt(idcard_array[8]) * 6 + parseInt(idcard_array[9]) * 3;
                Y = S % 11;
                M = "F";
                JYM = "10X98765432";
                M = JYM.substr(Y, 1);
                if (M == idcard_array[17]) {
                    if (parseInt(idcard_array[16]) % 2 == 0) {
                        sex_val = 'f';
                    } else {
                        sex_val = 'm';
                    }
                    if (sexE) {
                        //sexE.find('#sex_select').text(sex_val);
                        sexE.find('input[name^=person_sex]').each(function(){
                            if($(this).val()==sex_val){
                                //$(this).attr('checked','checked');
                                this.checked = true;
                                return false;
                            }
                        });
                    }
                    birthdayE && birthdayE.val(idcard.substr(6, 4) + '-' + idcard.substr(10, 2) + '-' + idcard.substr(12, 2));
                    birthdayE && birthdayE.parent().find('div.input-tips').remove();
                    return true;
                } else {
                    return false;
                }
            } else {
                return false;
            }
        default:
            return false;
            break;
        }
    };


    jQuery.validator.addMethod("checkMobile", function(value, element) {
        return  checkMobile(value);
    }, "请填写正确的手机号");

    jQuery.validator.addMethod("checkCredentials", function(value, element) {
        return checkIdcardOrder(value, element, $(element).parents('div.form-field').next(), $(element).parents('div.form-field').next().next().find('input[name^=person_birthday]'));
    }, '请填写正确的证件号码');


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


        $('#xorder_form').validate({
            highlight: false,
            unhighlight: false,
            errorClass: 'input-tips',
            errorElement: 'div',

            submitHandler: function(form) {
                if (!$("#checkbox").is(":checked")) {
                    alert("请阅读相关协议及合同");
                    return false;
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
                        else {
                            location.href = data.data.url;
                        }

                    },
                    error: function (XMLHttpRequest, textStatus, errorThrown) {
                        alert('订单提交失败');
                    },
                });
            },
        });

    });


    //右侧浮动开始
    $(function(){
        var rslidet = $(".order-slide").offset().top - 10;
        $(window).scroll(function() {
            if ($(document).scrollTop() > rslidet) {
                $(".order-info-wrap").css({top: "10px", position: "fixed"});
            } else {
                $(".order-info-wrap").removeAttr("style");
            }
        });
    });

    // 金额相关
    var equip_rent = {}
    for (var i=0; i<equipments.length; i++) {
        equip_rent['equipment_'+equipments[i]['id']] = equipments[i]['rent'];
    }

    var set_pay_info = function() {
        var total_price = price * num_apply;
        var total_rent = 0;
        var inputs_equip = $('.pasger-form-2 input.num');
        for (var i=0; i<inputs_equip.length; i++){
            total_rent += parseInt($(inputs_equip[i]).val()) * equip_rent[$(inputs_equip[i]).attr('name')];
        }


        $('#right_rent  span').text(total_rent);
        $('#good_total_right span').text(total_price + total_rent);

    };


    $(function() {
        set_pay_info();
        start_counter_select($('.pasger-form-2 .counter-select'), set_pay_info);
    });

})();
