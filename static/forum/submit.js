;
var member_submit_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $(".ca-input-box .submit").click(function (message){
            var btn_target = $(this);
            if( btn_target.hasClass("disabled") ){
                alert( "正在处理！！请不要重复点击~~" );
                return;
            }

            var title = $(".ca-input-box input[name=title]").val();
            var file=$(".ca-input-box input[type='file']")[0].files[0];


            var option=$(".ca-input-box .form-group select[name=option]").val();
            var option_string;
            if(option==="经济专栏"){
                 option_string="main";
            }else if (option==="经济杂谈"){
                option_string="chat";
            }else if(option==="行业观察"){
                option_string="observation";
            }else if (option==="案例分析"){
                option_string="analysis";
            }

            var content=$(".ca-input-box textarea[name=msg]").val();


            var login_name=$(".sq-quote .username").text();

            var formData = new FormData();
            formData.append("file",file);
            formData.append("title",title);
            formData.append("option",option);
            formData.append("content",content);
            formData.append("login_name",login_name);
            formData.append("status",1);
            formData.append("option_string",option_string)



            btn_target.addClass("disabled");
            $.ajax({
                url: common_ops.buildUrl( "/StockStar/publish" ),
                type: "POST",
                data:formData,
                contentType:false,
                processData : false,
                dataType:"json",

                success:function( res ){
                    btn_target.removeClass("disabled");
                    var callback = null;
                    if( res.code === 200 ){
                        callback = function(){
                            window.location.href = common_ops.buildUrl( "/StockStar/forum" );
                        };
                    }

                    common_ops.commom_alert(res.msg, callback)

                }
            });

        } );
    }
};

$(document).ready( function(){
    member_submit_ops.init();
});