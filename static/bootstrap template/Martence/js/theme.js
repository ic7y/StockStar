// -----------------------------

//   js index
/* =================== */
/*  
    

    

*/
// -----------------------------


(function ($) {
    "use strict";


    /*---------------------
    handler
    --------------------- */
    $(window).on('load', function () {
        nhPreloader();
        bpMenuareaFixed();
        bpMenuareaFixed2();
        bpMenuareaFixed3();
        bpCounterUphendle();
        bpSmoothhendle();
    });


    /*---------------------
    preloader
    --------------------- */
    function nhPreloader() {
        if ($('#preloader').length) {
            $('#preloader').fadeOut('slow', function () {
                $(this).remove();
            });
        }
    }

    /*----------------------------
    slick nav
    ------------------------------ */
    $('.menu').slicknav({
        prependTo: '.responsive-menu',
        label: '',
        allowParentLinks: true
    });

    /*------------------------
    meanmenu-remove-class
    ------------------------*/
    $(window).on('resize', function () {
        var wWidth = $(this).width();

        if (wWidth < 991) {
            // removing class
            $('.drop').addClass('m-d-removed');
            $('.m-d-removed').removeClass('drop');

            $('.third').addClass('t-h-m-removed');
            $('.t-h-m-removed').removeClass('third');

            $('.mega-menu').addClass('m-g-removed');
            $('.m-g-removed').removeClass('mega-menu');
        } else {
            // adding class
            $('.m-d-removed').addClass('drop');
            $('.drop').removeClass('m-d-removed');

            $('.third').removeClass('t-h-m-removed');
            $('.t-h-m-removed').addClass('third');

            $('.mega-menu').removeClass('m-g-removed');
            $('.m-g-removed').addClass('mega-menu');
        }
    }).resize();

    /*-----------------
    sticky
    -----------------*/
    function bpMenuareaFixed() {
        if ($('.header-bottom-area').length) {
            $(window).on('scroll', function () {
                if ($(window).scrollTop() > 160) {
                    $('.header-bottom-area').addClass('navbar-fixed-top');
                } else {
                    $('.header-bottom-area').removeClass('navbar-fixed-top');
                }
            });
        }
    }

    /*-----------------
    h2-sticky
    -----------------*/
    function bpMenuareaFixed2() {
        if ($('.h2-header-bottom-area').length) {
            $(window).on('scroll', function () {
                if ($(window).scrollTop() > 200) {
                    $('.h2-header-bottom-area').addClass('navbar-fixed-top');
                } else {
                    $('.h2-header-bottom-area').removeClass('navbar-fixed-top');
                }
            });
        }
    }

    /*-----------------
    h3-sticky
    -----------------*/
    function bpMenuareaFixed3() {
        if ($('.h3-header-bottom-area').length) {
            $(window).on('scroll', function () {
                if ($(window).scrollTop() > 140) {
                    $('.h3-header-bottom-area').addClass('navbar-fixed-top');
                } else {
                    $('.h3-header-bottom-area').removeClass('navbar-fixed-top');
                }
            });
        }
    }

    /*-----------------
    scroll-up
    -----------------*/
    $.scrollUp({
        scrollText: '<i class="fa fa-arrow-up" aria-hidden="true"></i>',
        easingType: 'linear',
        scrollSpeed: 1500,
        animation: 'fade'
    });

    /*------------------------------
         counter
    ------------------------------ */
    function bpCounterUphendle() {
        $('.counter-up').counterUp();
    };

    /*---------------------
    smooth scroll
    --------------------- */
    function bpSmoothhendle() {
        $('.smoothscroll').on('click', function (e) {
            e.preventDefault();
            var target = this.hash;

            $('html, body').stop().animate({
                'scrollTop': $(target).offset().top - 80
            }, 1200);
        });
    }

    /*---------------------
    countdown
    --------------------- */
    $('[data-countdown]').each(function () {
        var $this = $(this),
            finalDate = $(this).data('countdown');
        $this.countdown(finalDate, function (event) {
            $this.html(event.strftime('<span class="cdown days"><span class="time-count">%-D</span> <p>Days</p></span> <span class="cdown hour"><span class="time-count">%-H</span> <p>Hours</p></span> <span class="cdown minutes"><span class="time-count">%M</span> <p>MINUTES</p></span> <span class="cdown second"> <span><span class="time-count">%S</span> <p>seconds</p></span>'));
        });
    });

    /*---------------------
    fancybox
    --------------------- */
    $('[data-fancybox]').fancybox({
        image: {
            protect: true
        }
    });


    /*---------------------
    video-popup
    --------------------- */
    $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
        disableOn: 700,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 300,
        preloader: false,
        fixedContentPos: false
    });

    /*---------------------
    progress
    --------------------- */
    $('.all-progess').waypoint(function () {
        $('.progress-bar').addClass('left-anim');
    }, {
        triggerOnce: true,
        offset: '50%'
    });

    /*---------------------
    isotope
    --------------------- */
    $('#container').imagesLoaded(function () { //image loaded

        // filter items on button click
        $('.portfolio-menu').on('click', 'button', function () {
            var filterValue = $(this).attr('data-filter');
            $grid.isotope({
                filter: filterValue
            });
            $('.portfolio-menu').find('.checked').removeClass('checked');
            $(this).addClass('checked');
        });

        // masonary activation
        var $grid = $('.grid_container').isotope({
            itemSelector: '.grid',
            percentPosition: true,
            masonry: {
                // use outer width of grid-sizer for columnWidth
                columnWidth: '.grid'
            }
        })
    });

    /*---------------------
    slider-area
    --------------------- */
    function slider_area() {
        var owl = $(".slider-area");
        owl.owlCarousel({
            loop: true,
            margin: 0,
            responsiveClass: true,
            navigation: true,
            navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            nav: false,
            items: 1,
            smartSpeed: 1000,
            dots: true,
            autoplay: true,
            autoplayTimeout: 4000,
            center: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1
                },
                760: {
                    items: 1
                }
            }
        });
    }
    slider_area();

    /*---------------------
    testimonial-carousel
    --------------------- */
    function testimonial_carousel() {
        var owl = $(".testimonial-carousel");
        owl.owlCarousel({
            loop: true,
            margin: 0,
            responsiveClass: true,
            navigation: true,
            navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            nav: true,
            items: 2,
            smartSpeed: 2000,
            dots: false,
            autoplay: true,
            autoplayTimeout: 4000,
            center: false,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1
                },
                760: {
                    items: 2
                }
            }
        });
    }
    testimonial_carousel();

    /*---------------------
    brand-carousel
    --------------------- */
    function brand_carousel() {
        var owl = $(".brand-carousel");
        owl.owlCarousel({
            loop: true,
            margin: 20,
            responsiveClass: true,
            navigation: true,
            navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            nav: false,
            items: 5,
            smartSpeed: 2000,
            dots: false,
            autoplay: true,
            autoplayTimeout: 4000,
            center: false,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 2
                },
                760: {
                    items: 4
                },
                992: {
                    items: 5
                }
            }
        });
    }
    brand_carousel();

    /*---------------------
    h2-testimonial-carousel
    --------------------- */
    function h2_testimonial_carousel() {
        var owl = $(".h2-testimonial-carousel");
        owl.owlCarousel({
            loop: true,
            margin: 0,
            responsiveClass: true,
            navigation: true,
            navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            nav: false,
            items: 3,
            smartSpeed: 2000,
            dots: true,
            autoplay: true,
            autoplayTimeout: 4000,
            center: false,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1
                },
                760: {
                    items: 2
                },
                992: {
                    items: 3
                }
            }
        });
    }
    h2_testimonial_carousel();

    /*---------------------
    h2-portfolio-carousel
    --------------------- */
    function h2_portfolio_carousel() {
        var owl = $(".h2-portfolio-carousel");
        owl.owlCarousel({
            loop: true,
            margin: 20,
            responsiveClass: true,
            navigation: true,
            navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            nav: false,
            items: 5,
            smartSpeed: 2000,
            dots: true,
            autoplay: true,
            autoplayTimeout: 4000,
            center: false,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1
                },
                760: {
                    items: 4
                },
                992: {
                    items: 5
                }
            }
        });
    }
    h2_portfolio_carousel();


    /*---------------------
    h3-slider-area
    --------------------- */
    function h3_slider_area() {
        var owl = $(".h3-slider-area");
        owl.owlCarousel({
            loop: true,
            margin: 0,
            responsiveClass: true,
            navigation: true,
            navText: ["<i class='fas fa-long-arrow-alt-left'></i>", "<i class='fas fa-long-arrow-alt-right'></i>"],
            nav: true,
            items: 1,
            smartSpeed: 1000,
            dots: false,
            autoplay: true,
            autoplayTimeout: 4000,
            center: true,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1
                },
                760: {
                    items: 1
                }
            }
        });
    }
    h3_slider_area();

    /*---------------------
    h3-testimonial-carousel
    --------------------- */
    function h3_testimonial_carousel() {
        var owl = $(".h3-testimonial-carousel");
        owl.owlCarousel({
            loop: true,
            margin: 20,
            responsiveClass: true,
            navigation: true,
            navText: ["<i class='fa fa-angle-left'></i>", "<i class='fa fa-angle-right'></i>"],
            nav: true,
            items: 3,
            smartSpeed: 2000,
            dots: false,
            autoplay: true,
            autoplayTimeout: 4000,
            center: false,
            responsive: {
                0: {
                    items: 1
                },
                480: {
                    items: 1
                },
                760: {
                    items: 2
                },
                992: {
                    items: 3
                }
            }
        });
    }
    h3_testimonial_carousel();

    /*---------------------
    // Ajax Contact Form
    --------------------- */

    $('.cf-msg').hide();
    $('form#cf button#submit').on('click', function () {
        var fname = $('#fname').val();
        var phone = $('#phone').val();
        var email = $('#email').val();
        var msg = $('#msg').val();
        var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;

        if (!regex.test(email)) {
            alert('Please enter valid email');
            return false;
        }

        fname = $.trim(fname);
        phone = $.trim(phone);
        email = $.trim(email);
        msg = $.trim(msg);

        if (fname != '' && email != '' && msg != '') {
            var values = "fname=" + fname + "&phone=" + phone + "&email=" + email + " &msg=" + msg;
            $.ajax({
                type: "POST",
                url: "mail.php",
                data: values,
                success: function () {
                    $('#fname').val('');
                    $('#phone').val('');
                    $('#email').val('');
                    $('#msg').val('');

                    $('.cf-msg').fadeIn().html('<div class="alert alert-success"><strong>Success!</strong> Email has been sent successfully.</div>');
                    setTimeout(function () {
                        $('.cf-msg').fadeOut('slow');
                    }, 4000);
                }
            });
        } else {
            $('.cf-msg').fadeIn().html('<div class="alert alert-danger"><strong>Warning!</strong> Please fillup the informations correctly.</div>')
        }
        return false;
    });

    /*---------------------
    parallax
    --------------------- */
    $('.counter-area').parallax("50%", -.2);



}(jQuery));