// :::::ПРЕЛОАДЕР:::::
$(window).on('load', function () {
	// :::::СКРОЛЛБАР:::::     $(selector).mCustomScrollbar("scrollTo",position,options); - для прокрутки страницы через код | подробнее: http://manos.malihu.gr/jquery-custom-content-scroller/
	$("body").mCustomScrollbar({
		theme:"rounded-dots",
		scrollInertia:1000
	});
	var $preloader = $('#p_prldr'),
	    $svg_anm   = $preloader.find('.svg_anm');
	$svg_anm.fadeOut();
	$preloader.delay(500).fadeOut('slow');
});

function initBootstrapForms() {
    $("form.bootstrap-form").find("input,textarea").addClass("form-control");
    $("form.bootstrap-form").find("input[type='submit']").removeClass("form-control");
}

// :::::ОСНОВНЫЕ СКРИПТЫ:::::
$(document).ready(function() {

initBootstrapForms();
// $svg_anm.fadeIn(100);
// $preloader.fadeIn(100);

// $svg_anm.delay(700).fadeOut('slow');
// $preloader.delay(700).fadeOut('slow');

// :::::УПРАВЛЕНИЕ СОМ ПОРТОМ:::::
$('.container').on('click','.comajax div div button', function(){
		// ev.preventDefault();
		console.log('start...');
		var val;
		val = $(this).attr("value");
		$.post('../static/manage_action.php', {btn_mode: val}, 
			function() {
				console.log('Work!!!');
			}
			);
		return false;
	});



// :::::НАВИГАЦИОННАЯ ПАНЕЛЬ:::::
$('.navbar-nav li a').on('click', function(){
	console.log('hide');
	$('.navbar-collapse').collapse('hide');
});




$('#main-nav li a').on('click', function() {
	var href = $(this).attr('href');
	if(href == 'ambibox.php'){
		console.log('ambibox...');
		$.ajax({
			type: 'HEAD',
			url: 'http://yoursite.com/page.html',
			success: function() {
				console.log('bad');
			},
			error: function() {
				console.log('good');
			}
		});
	}
});
});