$(function () {
    $('.addToCartBtn').on("click",function (e) { 
        e.preventDefault();
        
        let product_id = $(this).closest('.product_data').find(".prod_id").val();
        let product_qty = $(this).closest('.product_data').find(".qty-input").val();
        let token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method:"POST",
            url:"/add-to-cart",
            data:{
                'product_id':product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken :token
            },
            success:function(response){
                alertify.success(response.status);
            }
        });
    });
    $('.changeQuantity').on("click",function (e) { 
        e.preventDefault();
        
        let product_id = $(this).closest('.product_data').find(".prod_id").val();
        let product_qty = $(this).closest('.product_data').find(".qty-input").val();
        let token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method:"POST",
            url:"/update-cart",
            data:{
                'product_id':product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken :token
            },
            success:function(response){
                // alertify.success(response.status);
            }
        });
    });
    $('.delete-cart-item').on("click",function (e) { 
        e.preventDefault();
        
        let product_id = $(this).closest('.product_data').find(".prod_id").val();
        let token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method:"POST",
            url:"/delete-cart-item",
            data:{
                'product_id':product_id,
                csrfmiddlewaretoken :token,
            },
            success:function(response){
                alertify.success(response.status);
                $(".cartdata").load(location.href + " .cartdata")
            }
        });
    });
});