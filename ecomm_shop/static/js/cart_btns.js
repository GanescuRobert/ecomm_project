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
                console.log(response);
                alertify.success(response.status);
            }
        });
    });
});