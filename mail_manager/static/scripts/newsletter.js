$(document).ready(function () {
    function loadNewsletters() {
        $.get("get_newsletters/", function (data) {
            var container = $("#newslettersContainer");
            container.empty();
            container.html(data.newsletters);
        });
    }

    loadNewsletters();

    function initCKEditor() {
        CKEDITOR.replace("content");
    }

    function destroyCKEditor() {
        if (CKEDITOR.instances["content"]) {
            CKEDITOR.instances["content"].destroy(true);
        }
    }

    $(document).on("click", ".edit-newsletter", function () {
        var id = $(this).data("id");
        var name = $(this).data("name");
        var content = $(this).data("content");

        $("#newsletterModalTitle").text("Редактировать рассылку");
        $("#newsletterId").val(id);
        $("#name").val(name);
        destroyCKEditor();
        initCKEditor();
        CKEDITOR.instances["content"].setData(content);

        $("#newsletterSubmitBtn").text("Сохранить");
        $("#newsletterModal").modal("show");
    });

    $(".btn-newsletter").click(function () {
        $("#newsletterModalTitle").text("Создать рассылку");
        $("#newsletterId").val("");
        $("#name").val("");
        destroyCKEditor();
        initCKEditor();
        CKEDITOR.instances["content"].setData("");

        $("#newsletterSubmitBtn").text("Создать");
        $("#newsletterModal").modal("show");
    });

    $("#newsletterForm").submit(function (event) {
        event.preventDefault();

        var id = $("#newsletterId").val();
        var url = id ? "edit/" : "create/";
        var content = CKEDITOR.instances["content"].getData();

        $.ajax({
            type: "POST",
            url: url,
            data: $(this).serialize() + "&content=" + encodeURIComponent(content),
            success: function (response) {
                alert(id ? "Рассылка обновлена!" : "Рассылка создана!");
                $("#newsletterModal").modal("hide");
                $("#newsletterForm")[0].reset();
                destroyCKEditor();
                initCKEditor();
                loadNewsletters();
            },
            error: function () {
                alert("Ошибка!");
            }
        });
    });
});