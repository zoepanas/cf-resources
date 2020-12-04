var search_templates = function (term) {
  window.location.href = `/search-templates?s=${term}`;
};

$(document).ready(function () {
  $("#search-template-btn").click(function () {
    var search_term = $("#template-search-term").val();
    search_templates(search_term);
  });

  $(".temp-card").click(function () {
    var link = $(this).attr("value");
    window.location.href = link;
  });
});
