var search_guides = function (term) {
  window.location.href = `/search?s=${term}`;
};

function guideSubmitted() {
  $("#add-guide-modal").hide();
  $("#guide-submitted-modal").show();
}

// function returns current date and time
function currentDT() {
  var date = Date();
  return date;
}

function sendEmail() {
  var title = $("#guide-title").val();
  var link = $("#guide-link").val();
  var image = $("#guide-image").val();
  var name = $("#fridge-name").val();
  var email = $("#fridge-email").val();
  var time = currentDT();
  Email.send({
    Host: "smtp.gmail.com",
    Username: "cf.resources.nyc@gmail.com",
    Password: "PITfall2020",
    To: "cf.resources.nyc@gmail.com",
    From: "cf.resources.nyc@gmail.com",
    Subject: "Resource Guide Submission",
    Body:
      "Guide Title: " +
      title +
      "<br> Link to Guide: " +
      link +
      "<br> Associated Image: " +
      image +
      "<br> Fridge Name: " +
      name +
      "<br> Associated Email: " +
      email +
      "<br>Time submitted: " +
      time,
  }).then(guideSubmitted());
}

$(document).ready(function () {
  $(".guide-object").click(function () {
    var link = $(this).attr("value");
    window.location.href = link;
  });

  $("#add-guide-btn").click(function () {
    console.log("showing");
    $("#add-guide-modal").show();
  });

  $("#submit-guide-btn").click(function () {
    console.log("sending email!");
    sendEmail();
  });

  $("#search-guide-btn").click(function () {
    var search_term = $("#guide-search-term").val();
    search_guides(search_term);
  });

  $(".close").click(function () {
    $("#add-guide-modal").hide();
  });

  $(window).click(function () {
    $("add-guide-modal").hide();
  });

  $("#myModal").on("shown.bs.modal", function () {
    $("#myInput").trigger("focus");
  });
});
