/* links input fields to their respective variables within
   the template text; only needs to be run once */
function format_template() {
    $(".customize-input-field").each(function (index) {
        var placeholder = $(this).attr("placeholder")
        console.log("placeholder = "+placeholder)
        var i = index
        $(".template-custom-item").each(function (index) {
            console.log("here")
            var str = $(this).text()
            str = str.replace(/[\[\]']+/g,'');
            console.log("str = "+str)
            if (placeholder.equals(str)){
                console.log(str)
                $(this).addClass(i)
            }
        })
    })
}

/* customizes template variables with user inputs */
function customize_template() {
    //
}

$(document).ready(function () {
    format_template()
    $("#template-text").html(text)
    $(".submit-btn").click(function () {
        customize_template();
    })
});