$(document).ready(function () {
  $(".guide-object").click(function () {
    var link = $(this).attr("value");
    console.log("guide link: ", link);
    window.location.href = link;
  });
});
