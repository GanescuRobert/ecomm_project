$(function () {
    $(document).on("click", ".payWithRazorpay", function (e) {
        e.preventDefault();

        let fname = $("[name='fname']").val();
        let lname = $("[name='lname']").val();
        let email = $("[name='email']").val();
        let phone = $("[name='phone']").val();
        let other = $("[name='other']").val();
        let city = $("[name='city']").val();
        let state = $("[name='state']").val();
        let country = $("[name='country']").val();
        let zipcode = $("[name='zipcode']").val();
        let token = $("[name='csrfmiddlewaretoken']").val();

        if (fname == "" || lname == "" || email == "" || phone == "" || other == "" || city == "" || state == "" || country == "" || zipcode == "") {
            swal("Alert!", "All fields are mandatory!", "error");
            return false;
        } else {
            $.ajax({
                method: "GET",
                url: "/proceed-to-pay",
                success: function (response) {
                    console.log(response);

                     // ! API key
                    let options = {
                        "key": "your_api_key", // Enter the Key ID generated from the Dashboard
                        "amount": response.total_price * 100, // Amount is in currency subunits. Default currency is INR. Hence, 50000 refers to 50000 paise
                        "currency": "USD",
                        "name": "G.R.",
                        "description": "Thank you for buying from us",
                        "image": "https://example.com/your_logo",
                        // "order_id": "order_9A33XWu170gUtm", //This is a sample Order ID. Pass the `id` obtained in the response of Step 1
                        "handler": function (response_handler) {
                            alert(response_handler.razorpay_payment_id);
                            const data = {
                                "fname": fname,
                                "lname": lname,
                                "email": email,
                                "phone": phone,
                                "other": other,
                                "city": city,
                                "state": state,
                                "country": country,
                                "zipcode": zipcode,
                                "payment_mode": "Paid by Razorpay",
                                "payment_id": response_handler.razorpay_payment_id,
                                csrfmiddlewaretoken: token,
                            }
                            $.ajax({
                                type: "POST",
                                url: "/place-order",
                                data: data,
                                dataType: "dataType",
                                success: function (response_place_order) {
                                    swal("Congratulations!", response_place_order.status, "success")
                                    .then((value)=>{
                                        window.location.href = "/my-orders"
                                    })
                                }
                            });

                        },
                        "prefill": {
                            "name": fname + ' ' + lname,
                            "email": email,
                            "contact": phone
                        },

                        "theme": {
                            "color": "#3399cc"
                        }
                    };
                    let rzp1 = new Razorpay(options);
                    rzp1.open();
                }
            });
        }
    });

});