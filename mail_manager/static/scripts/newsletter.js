$(document).ready(function () {
    function loadNewsletters() {
        $.get("get_newsletters/", function (data) {
            var container = $("#newslettersContainer");
            container.empty();
            container.html(data.newsletters);
        });
    }

    loadNewsletters();

    $(document).on("click", ".edit-newsletter", function () {
        var id = $(this).data("id");
        var name = $(this).data("name");
        var content = $(this).data("content");

        $("#newsletterModalTitle").text("Редактировать рассылку");
        $("#newsletterId").val(id);
        $("#name").val(name);
        $("#content").val(content);
        $("#newsletterSubmitBtn").text("Сохранить");

        $("#newsletterModal").modal("show");
    });

    $(".btn-newsletter").click(function () {
        $("#newsletterModalTitle").text("Создать рассылку");
        $("#newsletterId").val("");
        $("#name").val("");
        $("#content").val("");
        $("#newsletterSubmitBtn").text("Создать");

        $("#newsletterModal").modal("show");
    });

    $("#newsletterForm").submit(function (event) {
        event.preventDefault();

        var id = $("#newsletterId").val();
        var url = id ? "edit/" : "create/";

        $.ajax({
            type: "POST",
            url: url,
            data: $(this).serialize(),
            success: function (response) {
                alert(id ? "Рассылка обновлена!" : "Рассылка создана!");
                $("#newsletterModal").modal("hide");
                $("#newsletterForm")[0].reset();
                loadNewsletters();
            },
            error: function () {
                alert("Ошибка!");
            }
        });
    });
});