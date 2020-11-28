// function to show guides

$(document).ready(function () {
  $("#templates-link").click(function () {
    window.location.href = "http://127.0.0.1:5000/templates";
  });

  $("#guides-link").click(function () {
    window.location.href = "http://127.0.0.1:5000/guides";
  });

  $("#forum-link").click(function () {
    window.location.href = "http://127.0.0.1:5000/forum";
  });
});
