$(function () {
    var sku_ids = new Array();
    var i = 0;
    var count = 0;
    var zong = 0;
    $(".checkbox_i").click(function () {
        sku_ids = new Array();
        i = 0;
        count = 0;
        zong = 0;
        var counts = $("input[name='checkbox_i']:checkbox").length;
        $("input[name='checkbox_i']:checked").each(function () {
            var sku = $(this).attr("sku_id");
            zong += Number($("h6[sku_id|=" + sku + "]").text());
            sku_ids[i] = sku;
            i++;
            count += Number($("input[sku|=" + sku + "]").val());
        });

        if (i == counts) {
            $("input[name='checkbox_all']").prop('checked', true);
//             alert($("input[name='checkbox_all']").prop('checked'))
        } else {
            $("input[name='checkbox_all']").prop('checked', false);
        }
        // alert(i)
        $(".count").text(count);
        $(".zong").text(zong + ".00￥")
    });

    $(".checkbox_all").click(function () {
        if ($(".checkbox_all").prop("checked") == true) {
            $(".checkbox_i").each(function () {
                if ($(this).prop("checked") == false) {
                    $(this).click()
                }
            })
        } else {
            $(".checkbox_i").each(function () {
                if ($(this).prop("checked") == true) {
                    $(this).click()
                }
            })
        }
    });

    $("#jiesuan").click(function () {
        for (i in sku_ids) {
            $("input[name='csrfmiddlewaretoken']").after("<input type='hidden' name='sku_ids' value='" + sku_ids[i] + "'>")
        }
    });

    $(".delete_sku").click(function () {
        var sku_id = $(this).attr("delect_id");
        $.post("/cart/delete", {
            'sku_id': sku_id,
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
        }, function (data) {
            if (data.res == 3) {
                alert(data.message);
                $(".count").text(data.total_count)
            } else {
                alert(data.errmsg)
            }
        })
    });

    $("#shdz").click(function () {
        $.get("address", function (data) {
            $("#dizhi").text(data.addr + " (" + data.receiver + "收)" + data.phone)
            // alert(data.address)
        })
    });

    $("#tjdz").click(function () {
        $.post("address", {
            'receiver': $("#receiver").val(),
            'addr': $("#addr").val(),
            'zip_code': $("#zip_code").val(),
            'phone': $("#phone").val(),
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
        }, function (data) {
            alert(data.errmsg);
            $("#shdz").click()
        })
    });


    // 后台减少商品
    $(".less_my").click(function () {
        var sku_id = $(this).attr("sku_id");
        var a = $("input[sku|=" + sku_id + "]").val();
        if (a > 1) {
            a--;
        }
        gengxin(sku_id, a)
    });

    // 更新功能
    function gengxin(sku_id, a) {
        $("input[sku|=" + sku_id + "]").val(a);
        $.post("/cart/update", {
            'count': a,
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'sku_id': sku_id,
        }, function (data) {
            if (data.res == 5) {
                // $(".count").text(data.total_count);
                var price = $("h6[price|=" + sku_id + "]").text();
                var xiaoji = price * a;
                $("h6[sku_id|=" + sku_id + "]").text(xiaoji + ".00")
            } else {
                alert(data.errmsg);
            }
        })
    }

    // 后台增加商品
    $(".add_my").click(function () {
        var sku_id = $(this).attr("sku_id");
        var a = $("input[sku|=" + sku_id + "]").val();
        a++;
        gengxin(sku_id, a)
    });


    // 减少
    $("#less").click(function () {
        var a = $("#Quantity").val();
        if (a > 1) {
            a--;
        }
        $("#Quantity").val(a);
        a = a + ".00";
        unit_price = $("#unit_price").text();
        $("#total").text(unit_price * a + ".00￥")
    });
    // 增加
    $("#add").click(function () {
        var a = $("#Quantity").val();
        a++;
        $("#Quantity").val(a);
        a = a + ".00";
        unit_price = $("#unit_price").text();
        $("#total").text(unit_price * a + ".00￥")
    });

    $("#add_cart").click(function () {
        $.post("/cart/add", {
            'sku_id': $(this).attr('sku_id'),
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'Quantity': $("#Quantity").val()
        }, function (data) {
            if (data.res == 5) {
                alert(data.message)
            } else {
                alert(data.errmsg)
            }
        })
    });

    $("#grxx").click(function () {
        window.location.href = "/user"
    });


    $("#shdz").click(function () {
        window.location.href = "/user/address"
    });

    $("#qbdd").click(function () {
        window.location.href = "/user/order/1"
    });

    $("#xdy").click(function () {
        window.location.href = "/user/order/merchant/1"
    });

    var addr_id;
    var pay_method;

    $("#queren").click(function () {
        $("input:checked").each(function () {
            if (count == 0) {
                addr_id = $(this).val()
            } else {
                pay_method = $(this).val()
            }
            count++;
        });
        $.post("/order/commit", {
            'addr_id': addr_id,
            'pay_method': pay_method,
            'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val(),
            'sku_ids': $("input[name='sku_ids']").val()
        }, function (data) {
            if (data.res == 5) {
                alert(data.message)
                window.location.href = "http://127.0.0.1/user/order/1"
            } else {
                alert(data.errmsg)
            }
        })
    });

    $('.status').each(function () {
        status = $(this).attr('status');
        if (status == 1) {
            $(this).text('去支付')
        } else if (status == 2) {
            $(this).text("已支付")
        }
    });

    $('.status').click(function () {
        status = $(this).attr('status');
        order_id = $(this).attr('order_id');
        if (status == 1) {
            csrf = $('input[name="csrfmiddlewaretoken"]').val();
            params = {'order_id': order_id, 'csrfmiddlewaretoken': csrf};
            $.post('/order/pay', params, function (data) {
                if (data.res == 4) {
                    alert(data.message);
                    location.reload();
                } else {
                    alert(data.errmsg)
                }
            })
        }
    });

    $('.order_status').click(function () {
        order_status = $(this).attr('order_status');
        order_sku_id = $(this).attr('order_sku_id');
        order_id = $(this).attr('order_id');
        if (order_status == 3) {
            csrf = $('input[name="csrfmiddlewaretoken"]').val();
            params = {
                'order_sku_id': order_sku_id,
                'order_id': order_id,
                'csrfmiddlewaretoken': csrf
            };
            $.post('/order/paysku', params, function (data) {
                if (data.res == 4) {
                    alert(data.message);
                    location.reload();
                } else {
                    alert(data.errmsg)
                }
            })
        } else if (order_status == 4) {
            location.href = '/order/comment/' + order_id + '/' + order_sku_id
        }
    });

    $('.order_status').click(function () {
        order_merchant_status = $(this).attr('order_merchant_status');
        order_merchant_sku_id = $(this).attr('order_merchant_sku_id');

        if (order_merchant_status == 2) {
            csrf = $('input[name="csrfmiddlewaretoken"]').val();
            params = {'order_sku_id': order_merchant_sku_id, 'csrfmiddlewaretoken': csrf};
            $.post('/order/skufahuo', params, function (data) {
                if (data.res == 4) {
                    alert(data.message);
                    location.reload();
                } else {
                    alert(data.errmsg)
                }
            })
        }
    })
});