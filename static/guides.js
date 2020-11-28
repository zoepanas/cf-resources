$(document).ready(function () {
  $(".guide-object").click(function () {
    var guide = $(this).attr("id");
    console.log("guide id: ", guide);
    window.location.href = `/view-guide/${guide}`;
  });
});
