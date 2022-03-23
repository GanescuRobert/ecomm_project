$(function () {
    $(document).on("click", ".add-to-wishlist", function (e) {
        e.preventDefault();

        let product_id = $(this).closest('.product_data').find(".prod_id").val();
        let token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/add-to-wishlist",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token
            },
            success: function (response) {
                alertify.success(response.status);
            }
        });
    });

    $(document).on("click", ".delete-wishlist-item", function (e) {
        e.preventDefault();
        let product_id = $(this).closest('.product_data').find(".prod_id").val();
        let token = $('input[name=csrfmiddlewaretoken]').val();

        $.ajax({
            method: "POST",
            url: "/delete-wishlist-item",
            data: {
                'product_id': product_id,
                csrfmiddlewaretoken: token,
            },
            success: function (response) {
                alertify.success(response.status);
                $(".wishdata").load(location.href + " .wishdata")
            }
        });
    });
})