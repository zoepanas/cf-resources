var new_fridge_tag = "";

var search_guides = function (term) {
  window.location.href = `/search-guides?s=${term}`;
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

function get_most_recent_guides() {
  window.location.href = `/most-recent`;
}

function get_by_fridge(fridge) {
  window.location.href = `/guides/fridge?f=${fridge}`;
}

function get_by_tag(tag) {
  window.location.href = `/guides/tag?t=${tag}`;
}

function sendEmail() {
  var title = $("#guide-title").val();
  var link = $("#guide-link").val();
  var image = $("#guide-image").val();
  var name = $("#fridge-name").val();
  var email = $("#fridge-email").val();
  var time = currentDT();
  var tag = new_fridge_tag;
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
      time +
      "<br>Guide Topic: " +
      tag,
  }).then(guideSubmitted());
}

$(document).ready(function () {
  $(".guide-object").click(function () {
    var link = $(this).attr("value");
    window.location.href = link;
  });

  $("#add-guide-btn").click(function () {
    console.log("add overlay");
    $(".gray-overlay").show();
    $("#add-guide-modal").show();
    //$("body").addClass("overlay");
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

  $("#got-it-btn").click(function () {
    $("#guide-submitted-modal").hide();
    $(".gray-overlay").hide();
  });

  $("#most-recent-guides").click(function () {
    get_most_recent_guides();
  });

  $(".filter-by-fridge").click(function () {
    var fridge = $(this).attr("value");
    get_by_fridge(fridge);
  });

  $(".filter-by-tag").click(function () {
    var tag = $(this).attr("value");
    get_by_tag(tag);
  });

  $(".tag-option").click(function () {
    new_fridge_tag = $(this).attr("value");
  });
});
