var create_post = function (txt){
    console.log(txt)

    /*var card = $("<div class='card'>")
    var card_body = $("<div class='card-body></div>")
    var title = $("<h5 class='card-title'>"+"You"+"</h5>")
    var subtitle = $("<h6 class='card-subtitle mb-2 text-muted'>"+"Posted just now"+"</h6>")
    var card_txt = $("<p class='card-text'>"+txt+"</p>")

    $(card_body).append(title)
    $(card_body).append(subtitle)
    $(card_body).append(card_txt)

    console.log(card_body)

    $(card).append(card_body)

    console.log(card)

    $("#posts").prepend(card)*/

    $("#new-post-txt").val("")
    $("#create-post").hide()
    $("#posts").prepend("<div>"+txt+"</div>")

}

$(document).ready(function () {
    $("#create-post").hide();
    $("#create-post-btn").click(function () {
      $("#create-post").show();
    });
    $("#post-btn").click(function () {
        console.log("post-btn clicked")
        create_post(
            $("#new-post-txt").val()
        )
    });
});
  