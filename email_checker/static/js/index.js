function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


$(document).ready(function() {
    $(".form-emails").submit(function(e){
        e.preventDefault();
        var email1 = $("#email1").val();
        var email2 = $("#email2").val();
        var email3 = $("#email3").val();
        var email4 = $("#email4").val();
        var email5 = $("#email5").val();
//        console email1;
        // put form data store in data object
        var data = {
            email1: email1,
            email2: email2,
            email3: email3,
            email4: email4,
            email5: email5,
        };
        // change data to json string
        var jsonData = JSON.stringify(data);
        $.ajax({
            url: "/api/v1.0/index",
            type: "post",
            data: jsonData,
            contentType: "application/json",
            dataType: "json",
            headers: {
                "X-CSRFToken": getCookie("csrf_token")
            },
            success: function (resp) {
                if (resp.errno == "0") {
                    location.href = "/api/v1.0/emails";
                } else {
                    alert(resp.errmsg);
                }
            }
        })
    });
})