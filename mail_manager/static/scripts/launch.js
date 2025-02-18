$(document).ready(function () {
    $(".btn-launch").click(function () {
        $("#newsletter_to_start_id").val("");
        $("#eta").val("");
        $("#countdown").val("");

        $("#launchModal").modal("show");
    });

    $("#launchForm").submit(function (event) {
        event.preventDefault();

        var url = "launch/";
        var formData = $(this).serialize();

        $.ajax({
            type: "POST",
            url: url,
            data: formData,
            success: function () {
                alert("Рассылка запущена!");
                $("#launchModal").modal("hide");
                $("#launchForm")[0].reset();
            },
            error: function () {
                alert("Ошибка!");
            }
        });
    });
});