;
var member_reg_ops = {
    init:function(){
        this.eventBind();
    },
    eventBind:function(){
        $(".reg_wrap .do-reg").click( function(){
            var btn_target = $(this);
            if( btn_target.hasClass("disabled") ){
                common_ops.alert( "正在处理！！请不要重复点击~~" );
                return;
            }

            var login_name = $(".reg_wrap input[name=login_name]").val();
            var login_pwd = $(".reg_wrap input[name=login_pwd]").val();
            var login_pwd2 = $(".reg_wrap input[name=login_pwd2]").val();
            //JS先于服务器进行数据格式校验
            if( login_name === undefined || login_name.length < 1 ){
                common_ops.alert( "请输入正确的用户名~~" );
                return ;
            }

            if( login_pwd === undefined || login_pwd.length < 6 ){
                common_ops.alert( "请输入正确的登录密码，并且不能小于6个字符~~" );
                return ;
            }

            if( login_pwd2 === undefined || login_pwd2 !==login_pwd ){
                common_ops.alert( "请重新确认密码~~" );
                return ;
            }
            btn_target.addClass("disabled");
            $.ajax({
                url: common_ops.buildUrl( "/StockStar/register" ),
                type: "POST",
                data:{

                    login_name:login_name,
                    login_pwd:login_pwd,
                    login_pwd2:login_pwd2,
                },
                dataType:'json',
                success:function( res ){
                    btn_target.removeClass("disabled");
                    //定义回调函数，在用户点击窗口上的确认按钮再进行页面重定向
                    var callback = null;
                    if( res.code === 200 ){
                        callback = function(){
                            window.location.href = common_ops.buildUrl( "/StockStar/login" );
                        };
                    }
                    common_ops.alert( res.msg,callback );
                }
            });

        } );
    }
};

$(document).ready( function(){
    member_reg_ops.init();
});