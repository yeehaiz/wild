/*
* eg
<link href="../../uploader/uploader.css" rel="stylesheet" />
<ul id="uploaderImg" class="uploader "></ul>
<div class="control-group">
<label class="control-label" for="productIntro">图片控件</label>
<div class="controls">
<ul id="uploaderImg" class="uploader"></ul>
</div>
</div>
<script>
$("#uploaderImg").uploader({
    maxLength: 2,
    name:'img_url',
    width:'80px',
    height:'80px'
});
</script>
*/
(function($){


    function UploadFile(options){

        var id = Math.random().toString(16).substring(2) + (+new Date());
        var html = '<div id="uploadSnfs'+id+'" style="display: none;">' +
            '<form id="formUploadSnfs'+id+'" class="uploadSnfs" target="frameUploadSnfs'+id+'" method="post" action="'+options.uploadUrl+'" enctype="multipart/form-data">'+
            '<input id="formUploadSnfsFile'+id+'" type="file" name="file" accept="image/jpeg,image/gif,image/png" />'+
            '</form>'+
            '<iframe id="frameUploadSnfs'+id+'" name="frameUploadSnfs'+id+'" style="display:none"></iframe>' +
            '</div>';
        var $uploadSnfs = $(html);
        $uploadSnfs.appendTo("body");

        var that = this;
        this.id = id;
        this.$formUploadSnfs = $("#formUploadSnfs"+id);
        this.$frameUploadSnfs = $("#frameUploadSnfs"+id);
        this.$file = $('#formUploadSnfsFile'+id);

        this.$file.on('change', function() {
            var $this = $(this);
            var fileName = $this.val();

            if(fileName == ''){
                return false;
            }

            that.$formUploadSnfs.submit();
        });

        //上传文件回调
        this.$frameUploadSnfs.load(function(){
            var $frame = $(window.frames['frameUploadSnfs'+id].document.body);
            //若iframe携带返回数据，为图片url
            var url = $frame.html().trim();
            if(url != '') {
                if($.isFunction(options.success)){
                    options.success(url);
                }
                $frame.html('');
                that.$file.val('');
            }else{
                if($.isFunction(options.error)){
                    options.error();
                }
            }
        });
    }

    UploadFile.prototype.selectFile = function(){
        this.$file.click();
    };

    $.fn.uploader = function(options, param){
        if (typeof options == 'string'){
            if ($.isFunction($.fn.uploader.methods[options])){
                return $.fn.uploader.methods[options](this, param);
            }
        }

        options = options || {};
        return this.each(function(){

            var $this = $(this);
            var opts = $.extend({}, $.fn.uploader.defaults, options);
            $this.html(template.compile(opts.tplAdd)({
                width:opts.width,
                height:opts.height
            }));

            var $tip = $(".uploader-tip", this);
            var $cancel = $(".uploader-cancel", this);
            var $add = $(".uploader-add", this);

            var uploadFileObj = new UploadFile($.extend({
                success:function(url){
                    $.fn.uploader.methods.addItem($this, url);
                },
                error:function(){
                    alert('上传文件失败，请重新上传');
                }
            }, opts));

            //添加图片
            $this.on("click", ".uploader-btn", function() {
                $this.addClass("uploader-uploading");
                uploadFileObj.selectFile();
                //选择文件
                $this.removeClass("uploader-uploading");
            });

            // 删除图片
            $this.on("click", ".uploader-del", function() {
                $.fn.uploader.methods.removeItem($this, $(this).closest("li[data-url]").attr("data-url"));
            });

            // 取消上传
            $this.on("click", ".uploader-cancel", function() {
                $this.removeClass("uploader-uploading");
                return false;
            });

            $(this).data('options',opts);
        });
    };

    $.fn.uploader.methods = {
        options: function($target){
            return $.data($target[0], 'options');
        },
        getValue:function($target, split){
            return this.getValues($target).join( split || ',');
        },
        getValues: function($target){
            var values = [];
            $target.find('li[data-url]').each(function() {
                values.push($(this).attr("data-url"));
            });
            return values;
        },
        setValues: function($target, values){
            this.clear($target);
            if(!$.isEmptyObject(values)){
                this.addItem($target, values);
            }
        },
        setValue:function($target, values){
            if(!$.isEmptyObject(values)){
                this.setValues($target, values.split(','));
            }else{
                this.clear($target);
            }
        },
        getSize: function($target) {
            return $target.find("li[data-url]").length;
        },
        //添加图片项
        addItem: function($target, url) {
            var options = this.options($target);
            if(!$.isArray(url)){
                url = [url];
            }
            if (options.maxLength < this.getSize($target)+url.length) {
                return;
            }
            var $add = $target.find(".uploader-add");
            var fn = template.compile(options.tplItem);
            $add.before(fn({
                name:options.name,
                url: url,
                width:options.width,
                height:options.height,
                maxLength:options.maxLength
            }));
            if (options.maxLength == this.getSize($target)) {
                $add.hide();
            }
        },
        //删除图片项
        removeItem: function($target, url) {
            var options = this.options($target);
            $target.find('li[data-url="' + url + '"]').remove();
            if (this.getSize($target) < options.maxLength) {
                $target.find(".uploader-add").show();
            }
        },
        isValid: function($target) {
            var options = this.options($target);
            var values = this.getValues($target);
            if(options.required && options.maxLength==0){
                return false;
            }

            if(options.maxLength<values.length){
                return false;
            }
            return true;
        },
        clear:function($target){
            $target.find('li[data-url]').remove();
        }
    };

    $.fn.uploader.defaults = {
        name:'',
        maxLength: 1,
        required:true,
        width:'140px',
        height:'140px',
        uploadUrl: '/admin/uploadimage/',
        tplAdd:'\
            <li class="uploader-add" style="width:{{width}};height:{{height}};">\
            <div class="uploader-btn"></div>\
                <span class="uploader-tip">上传中</span>\
                <a class="uploader-cancel" href="javascript:;"></a>\
            </li>',
        tplItem:'\
        {{each url}}\
        <li data-url="{{$value}}" style="width:{{width}};height:{{height}};">\
            <input type="hidden" name="{{name}}" value="{{$value}}" />\
            <img src="{{$value}}"  />\
            <a class="uploader-del" href="javascript:;"></a>\
            </li>\
        {{/each}}\
        '
    };

}(jQuery));
