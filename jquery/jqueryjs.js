$(document).ready(function () {

    //Question 01
    console.log("Hello World.");

    //Question 02
    $("#test").addClass(".load");

    //Question 03
    $("[class$=new]").css('color', 'red');

    //Question 04
    $(".submit_bt").attr('disabled', true);

    //Question 05
    $("#main > .target").css('font-size', '25px');

    //Question 06
    $("#changeme").replaceWith("<p>" + $("#changeme").html());

    //Questions 07 & 08
    $(".clickme").on('click', function (e) {
        $("#clickit").clone().insertAfter("#clickit").on('click', e.handleObj.handler);
    })

    //Question 09
    $(".Cars").on('change', function () {
        $('.info').html("<p> Selected car : " + this.value);
    })

    //Question 10
    $("#hoverhere").mouseover(function () {
        $(".Chocolate").toggle();
    })

    //Question 11
    $("#gtag").on("click", function (e) {
        e.preventDefault();
    })

    //Question 12
    $(".parentclass").click(function (e) {
        $(".bikes").css('color', 'red');
    })
    $(".bikes li").click(function (e) {
        e.stopPropagation();
    })

    //Question 13

    var max = 0
    $('body').children().each((i, val) => {
        ht = $(val).height()
        if (ht > max) {
            max = ht
        }
    })
    $('#max-height').html(max)

    //Question 14
    $("td").each(function (index, element) {
        var num = Number($(this).html());
        if (num > 10) {
            $(this).css("backgroundColor", "lightcoral");
        }
    })

    //Question 15

    $.ajax({
        url: 'https://github.com/bucc-sanyam/TTN/blob/html/htmlassignment',
        success: (res) => {
            $console.log(res)
            $('#ajax-res').html('An ajax request was successful, its result is in the console.')
        }
    });

    //Question 16

    $('.cross-button').on('click', (e) => {
        $.ajax({
            url: 'https://github.com/bucc-sanyam/TTN/blob/html/htmlassignment',
            success: (res) => {
                $(e.target).parent().remove()
            }
        })
    })

    //Question 17

    var imgSrc = ['1.jpg', '2.jpg', '3.jpg']
    var imgArr = [new Image(600, 400), new Image(600, 400), new Image(600, 400)]
    imgArr.forEach((img, i) => {
        img.src = imgSrc[i]
        $('#img-container').append(img)
        domImg = $('#img-container').children().last()
        domImg.css({ 'position': 'absolute', 'z-index': '0' })
        if (i !== imgArr.length - 1) {
            domImg.css('width', '0px')
        }
    })
    function initSlides(slide = $('#img-container img:first-child')) {
        let len = imgArr.length
        slideIndex = imgArr.indexOf(slide[0])

        prevIndex = '(' + ((slideIndex + len - 1) % len).toString() + ')'
        prevSlide = $('#img-container img:eq' + prevIndex)

        nextIndex = '(' + ((slideIndex + len + 1) % len).toString() + ')'
        nextSlide = $('#img-container img:eq' + nextIndex)

        slide.css('z-index', '1')
        prevSlide.css('z-index', '0')
        slide.animate({
            width: '600px'
        }, 3000, () => {
            setTimeout(() => {
                prevSlide.css('width', '0px')
                initSlides(nextSlide)
            }, 500)
        })
    }
    initSlides()

})

