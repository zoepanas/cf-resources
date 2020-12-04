/* links input fields to their respective variables within
   the template text on first run; every run, replaces customizable
   terms with user-inputted terms */

var search_templates = function (term) {
  window.location.href = `/search-templates?s=${term}`;
};

function customize_template() {
  $(".customize-input-field").each(function (index) {
    var placeholder = $(this).attr("placeholder");
    var replace_class = placeholder.replace(/\s+/g, "-").toLowerCase();
    var replace_with = $(this).val();
    $(this).val("");
    var i = index;
    $(".template-custom-item").each(function (index) {
      var str = $(this).text();
      str = str.replace(/[\[\]']+/g, "");
      if (placeholder === str || $(this).hasClass(replace_class)) {
        if (!$(this).hasClass(replace_class)) {
          $(this).addClass(replace_class);
        }
        $(this).text(replace_with);
      }
    });
  });
}

$(document).ready(function () {
  //$("#template-text").html(text);
  $(".submit-btn").click(function () {
    customize_template();
  });

  $("#search-template-btn").click(function () {
    var search_term = $("#template-search-term").val();
    search_templates(search_term);
  });
});
