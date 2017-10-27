$(function () {
    $(".datepicker").datepicker({
        dateFormat: "mm/dd/yy",
        showButtonPanel: true,
        showAnim: "slide",
    });
    var today = new Date();
    var new_date = new Date();
    new_date.setDate(today.getDate() + 1);
    $(".datepicker.check_in").datepicker("setDate", new Date());
    $(".datepicker.check_in").datepicker("option", "onSelect", function(dateText) {
        curr_date = $(".datepicker.check_in").datepicker("getDate");
        console.log(curr_date);
        var new_date = curr_date;
        new_date.setDate(curr_date.getDate() + 1);
        console.log(new_date);
        $(".datepicker.check_out").datepicker("setDate", new_date);
        $(".datepicker.check_out").datepicker("option", "minDate", new_date);
    });
    $(".datepicker.check_out").datepicker("setDate", new_date);
    $(".datepicker.check_out").datepicker("option", "minDate", new_date);
});

$(document).ready(function () {
    var action;
    $(".number-spinner button").mousedown(function () {
        btn = $(this);
        input = btn.closest('.number-spinner').find('input');
        btn.closest('.number-spinner').find('button').prop("disabled", false);

        if (btn.attr('data-dir') == 'up') {
            action = setInterval(function () {
                if (input.attr('max') == undefined || parseInt(input.val()) < parseInt(input.attr('max'))) {
                    input.val(parseInt(input.val()) + 1);
                } else {
                    btn.prop("disabled", true);
                    clearInterval(action);
                }
            }, 50);
        } else {
            action = setInterval(function () {
                if (input.attr('min') == undefined || parseInt(input.val()) > parseInt(input.attr('min'))) {
                    input.val(parseInt(input.val()) - 1);
                } else {
                    btn.prop("disabled", true);
                    clearInterval(action);
                }
            }, 50);
        }
    }).mouseup(function () {
        clearInterval(action);
    });

});

$(document).ready(function () {
    var container_width = SINGLE_IMAGE_WIDTH * $(".container-inner a").length;
    $(".container-inner").css("width", container_width);
});

$('#myCarousel').carousel({
    interval: 4000
});

