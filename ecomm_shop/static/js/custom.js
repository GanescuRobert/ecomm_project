$(function () {
    $('.increment-btn').on("click", function (e) {
        e.preventDefault();
        let inc_value = $(this).closest('.product_data').find('.qty-input').val();
        let value = Number(inc_value)
        value = isNaN(value) ? 0 : value;
        if (value < 10) {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });
    $('.decrement-btn').on("click", function (e) {
        e.preventDefault();
        let inc_value = $(this).closest('.product_data').find('.qty-input').val();
        let value = Number(inc_value)
        value = isNaN(value) ? 0 : value;
        if (value > 1) {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }
    });
  
})