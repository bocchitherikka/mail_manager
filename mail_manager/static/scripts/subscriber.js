function checkNewsletter(newsletterId) {
    return $.ajax({
        type: "GET",
        url: "/check_newsletter/" + newsletterId + "/",
    });
}

$(document).ready(function () {
    $(".btn-subscriber").click(function () {
        $("#sub_name").val("");
        $("#sub_surname").val("");
        $("#email").val("");
        $("#birth_date").val("");
        $("#newsletter_id").val("");

        $("#subscriberModal").modal("show");
    });

    $("#subscriberForm").submit(function (event) {
        event.preventDefault();

        var newsletterId = $("#newsletter_id").val();
        var url = "add_subscriber/";
        var formData = $(this).serialize();

        checkNewsletter(newsletterId)
            .done(function (response) {
                if (response.exists) {
        $.ajax({
            type: "POST",
            url: url,
            data: formData,
            success: function () {
                alert("Подписчик добавлен!");
                $("#subscriberModal").modal("hide");
                $("#subscriberForm")[0].reset();
            },
            error: function () {
                alert("Ошибка!");
            }
        });
                } else {
                    alert("Рассылка с таким ID не найдена!");
                }
            })
            .fail(function () {
                alert("Ошибка при проверке рассылки!");
            });
    });
});