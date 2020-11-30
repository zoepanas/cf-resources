function add_guide() {
  console.log("adding guide -- or trying");
  var guide_name = $("#guide_name").val();
  var link = $("#guide_link").val();
  var image = $("#guide_image").val();
  var email = $("#email").val();
  var contributor = $("#contributor").val();

  var guide = [guide_name, link, image, contributor, email];
  submit_guide(guide);
}

var search_guides = function (term) {
  window.location.href = `/search?s=${term}`;
};

var submit_guide = function (guide) {
  var guide_to_add = {
    guide_name: guide[0],
    link: guide[1],
    image: guide[2],
    contributor: guide[3],
    email: guide[4],
  };
  $.ajax({
    type: "POST",
    url: "submit-guide",
    dataType: "json",
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(guide_to_add),
    success: function (result) {
      console.log("added guide!");
    },
    error: function (request, status, error) {
      console.log("Error");
      console.log(request);
      console.log(status);
      console.log(error);
    },
  });
};

$(document).ready(function () {
  $(".guide-object").click(function () {
    var link = $(this).attr("value");
    window.location.href = link;
  });

  $("#add-guide-btn").click(function () {
    window.location.href = `/add-guide`;
  });

  $("#submit-guide-btn").click(function () {
    add_guide();
  });

  $("#search-guide-btn").click(function () {
    var search_term = $("#guide-search-term").val();
    search_guides(search_term);
  });
});
