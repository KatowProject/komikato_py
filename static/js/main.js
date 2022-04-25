/*
	Editorial by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/
const db = localStorage;

(function ($) {

	var $window = $(window),
		$head = $('head'),
		$body = $('body');

	// Breakpoints.
	breakpoints({
		xlarge: ['1281px', '1680px'],
		large: ['981px', '1280px'],
		medium: ['737px', '980px'],
		small: ['481px', '736px'],
		xsmall: ['361px', '480px'],
		xxsmall: [null, '360px'],
		'xlarge-to-max': '(min-width: 1681px)',
		'small-to-xlarge': '(min-width: 481px) and (max-width: 1680px)'
	});

	// Stops animations/transitions until the page has ...

	// ... loaded.
	$window.on('load', function () {
		window.setTimeout(function () {
			$body.removeClass('is-preload');
		}, 100);

		if (breakpoints.active('<=medium')) {
			$body.find(".table-wrapper.modl").attr("style", "overflow-y: scroll; height:400px; width:100%");
		} else {
			$body.find(".table-wrapper.modl").attr("style", "overflow-y: scroll; height:400px;");
		}

		const brightness = db.getItem("brightness");
		$(".chapter").css("-webkit-filter", `brightness(${brightness}%)`);

		$("body").on('DOMSubtreeModified', "output", function () {
			const value = $(this).text();
			db.setItem("brightness", value);
			$(".chapter").css("-webkit-filter", `brightness(${value}%)`);
		});
	});

	// ... stopped resizing.
	var resizeTimeout;

	$window.on('resize', function () {
		// Mark as resizing.
		$body.addClass('is-resizing');

		// Unmark after delay.
		clearTimeout(resizeTimeout);

		resizeTimeout = setTimeout(function () {
			$body.removeClass('is-resizing');
		}, 100);

	});

	// Fixes.

	// Object fit images.
	if (!browser.canUse('object-fit')
		|| browser.name == 'safari')
		$('.image.object').each(function () {

			var $this = $(this),
				$img = $this.children('img');

			// Hide original image.
			$img.css('opacity', '0');

			// Set background.
			$this
				.css('background-image', 'url("' + $img.attr('src') + '")')
				.css('background-size', $img.css('object-fit') ? $img.css('object-fit') : 'cover')
				.css('background-position', $img.css('object-position') ? $img.css('object-position') : 'center');

		});

	// Sidebar.
	var $sidebar = $('#sidebar'),
		$sidebar_inner = $sidebar.children('.inner');

	// Inactive by default on <= large.
	breakpoints.on('<=large', function () {
		$sidebar.addClass('inactive');
	});

	breakpoints.on('>large', function () {
		$sidebar.removeClass('inactive');
	});

	// Hack: Workaround for Chrome/Android scrollbar position bug.
	if (browser.os == 'android'
		&& browser.name == 'chrome')
		$('<style>#sidebar .inner::-webkit-scrollbar { display: none; }</style>')
			.appendTo($head);

	// Toggle.
	$('<a href="#sidebar" class="toggle">Toggle</a>')
		.appendTo($sidebar)
		.on('click', function (event) {

			// Prevent default.
			event.preventDefault();
			event.stopPropagation();

			// Toggle.
			$sidebar.toggleClass('inactive');

		});

	// Events.

	// Link clicks.
	$sidebar.on('click', 'a', function (event) {

		// >large? Bail.
		if (breakpoints.active('>large'))
			return;

		// Vars.
		var $a = $(this),
			href = $a.attr('href'),
			target = $a.attr('target');

		// Prevent default.
		event.preventDefault();
		event.stopPropagation();

		// Check URL.
		if (!href || href == '#' || href == '')
			return;

		// Hide sidebar.
		$sidebar.addClass('inactive');

		// Redirect to href.
		setTimeout(function () {

			if (target == '_blank')
				window.open(href);
			else
				window.location.href = href;

		}, 500);

	});

	// Prevent certain events inside the panel from bubbling.
	$sidebar.on('click touchend touchstart touchmove', function (event) {

		// >large? Bail.
		if (breakpoints.active('>large'))
			return;

		// Prevent propagation.
		event.stopPropagation();

	});

	// Hide panel on body click/tap.
	$body.on('click touchend', function (event) {

		// >large? Bail.
		if (breakpoints.active('>large'))
			return;

		// Deactivate.
		$sidebar.addClass('inactive');

	});

	// Scroll lock.
	// Note: If you do anything to change the height of the sidebar's content, be sure to
	// trigger 'resize.sidebar-lock' on $window so stuff doesn't get out of sync.

	$window.on('load.sidebar-lock', function () {

		var sh, wh, st;

		// Reset scroll position to 0 if it's 1.
		if ($window.scrollTop() == 1)
			$window.scrollTop(0);

		$window
			.on('scroll.sidebar-lock', function () {

				var x, y;

				// <=large? Bail.
				if (breakpoints.active('<=large')) {

					$sidebar_inner
						.data('locked', 0)
						.css('position', '')
						.css('top', '');

					return;

				}

				// Calculate positions.
				x = Math.max(sh - wh, 0);
				y = Math.max(0, $window.scrollTop() - x);

				// Lock/unlock.
				if ($sidebar_inner.data('locked') == 1) {

					if (y <= 0)
						$sidebar_inner
							.data('locked', 0)
							.css('position', '')
							.css('top', '');
					else
						$sidebar_inner
							.css('top', -1 * x);

				}
				else {

					if (y > 0)
						$sidebar_inner
							.data('locked', 1)
							.css('position', 'fixed')
							.css('top', -1 * x);

				}

			})
			.on('resize.sidebar-lock', function () {

				// Calculate heights.
				wh = $window.height();
				sh = $sidebar_inner.outerHeight() + 30;

				// Trigger scroll.
				$window.trigger('scroll.sidebar-lock');

			})
			.trigger('resize.sidebar-lock');

	});

	// Menu.
	var $menu = $('#menu'),
		$menu_openers = $menu.children('ul').find('.opener');

	// Openers.
	$menu_openers.each(function () {

		var $this = $(this);

		$this.on('click', function (event) {

			// Prevent default.
			event.preventDefault();

			// Toggle.
			$menu_openers.not($this).removeClass('active');
			$this.toggleClass('active');

			// Trigger resize (sidebar lock).
			$window.triggerHandler('resize.sidebar-lock');

		});

	});



})(jQuery);

$(document).ready(function () {

	$("#query").on("keyup", function (e) {
		const value = $(this).val();
		const source = $("#search").data("source");

		if (e.keyCode === 13) {
			if (value.length < 1) return;

			switch (source) {
				case 'komikindo':
					window.location.href = `/komikindo/search/${value}`;
					break;

				case 'otakudesu':
					window.location.href = `/otakudesu/search/${value}`;
					break;

				case 'mangabat':
					window.location.href = `/mangabat/search/${value}`;
			}
		}
	});

	$("#btn-brightness").on("click", function (e) {
		Swal.fire({
			title: 'Brightness',
			input: 'range',
			inputAttributes: {
				min: 0,
				max: 100,
				class: 'form-range',
				id: 'brightness',
				style: 'height: 0.25em; line-height: 0.25em;'
			},
			inputValue: db.getItem("brightness") || 100,
			showCancelButton: false,
			showConfirmButton: false,
		});

		$("output").css("line-height", "0.25em");
		$(".swal2-range").css("height", '');
	});

	$("#btn-option").on("click", async function (e) {
		const { value: option } = await Swal.fire({
			title: 'Select color',
			input: 'radio',
			inputValidator: (value) => {
				if (!value) {
					return 'You need to choose something!'
				}
			},
			didOpen: (e) => {
				const checkType = db.getItem("read-type");
				$(e).find(".swal2-confirm.swal2-styled").removeClass("swal2-styled").toggleClass("button");
				$(e).find(".swal2-radio").html(`
					<input type="radio" id="demo-priority-low" name="demo-priority" value="page" ${checkType === 'page' ? 'checked' : ''}>
					<label for="demo-priority-low">Page</label>

					<input type="radio" id="demo-priority-normal" name="demo-priority" value="webtoon" ${checkType === 'webtoon' ? 'checked' : ''}>
					<label for="demo-priority-normal">Webtoon</label>
				`)
			}
		});

		switch (option) {
			case 'page':
				db.setItem("read-type", "page");

				window.location.reload();
				break;

			case 'webtoon':
				db.setItem("read-type", "webtoon");

				window.location.hash = "";
				window.location.reload();
				break;
		}
	});

	$(".dropdown-item").on("click", async function (e) {
		const endpoint = window.location.pathname.split("/")[3];
		const query = $(this).data("query");

		const response = await $.getJSON(`/api/otakudesu/eps/${endpoint}/?id=${query}`);

		$(".chapter").html("");
		if (response.stream_link.includes("archive.org")) {
			$(".chapter").append(`
				<video id="player" playsinline controls data-poster="/assets/image/kato.png">
					<source src="${response.stream_link}" type="video/mp4" />  
				</video>
			`);
			var Player = new Plyr('#player');
		} else {
			$(".chapter").append(`
				<div class="embed-responsive embed-responsive-16by9">
					<iframe class="embed-responsive-item" src="${response.stream_link}" allowfullscreen></iframe>
				</div>
			`);
		}
	});

	$('#pop-carousel').carousel({
		interval: 10000
	})

	$('.carousel .carousel-item').each(function () {
		var minPerSlide = 3;
		var next = $(this).next();
		if (!next.length) {
			next = $(this).siblings(':first');
		}
		next.children(':first-child').clone().appendTo($(this));

		for (var i = 0; i < minPerSlide; i++) {
			next = next.next();
			if (!next.length) {
				next = $(this).siblings(':first');
			}

			next.children(':first-child').clone().appendTo($(this));
		}
	});

	const chapter = $(".chapter");
	const imgs = chapter.find("img");
	const type = db.getItem("read-type") || "webtoon";
	switch (type) {
		case 'webtoon':
			$(imgs).each(function (e) {
				$(this).css("display", "block");
			});
			break;

		case 'page':
			const hash = window.location.hash;
			if (hash)
				chapter.find(hash).css("display", "block");
			else
				chapter.find("img:first-child").css("display", "block");

			if ("onhashchange" in window) {
				window.onhashchange = function () {
					const hash = window.location.hash.substring(1);

					chapter.find("img[style='display: block;']").css("display", "none");
					chapter.find(`#${hash}`).css("display", "block");

					$("#page-pagination").text(`${hash.replace("page-", "")} / ${imgs.length}`);
				}
			}

			$(document).on("keyup", function (e) {
				if (e.keyCode === 37) {
					const findActive = chapter.find("img[style='display: block;']");
					const prev = findActive.prev();
					if (prev.length) {
						window.location.hash = prev.attr("id");
					}
				} else if (e.keyCode === 39) {
					const findActive = chapter.find("img[style='display: block;']");
					const next = findActive.next();
					if (next.length) {
						window.location.hash = next.attr("id");
					}
				}
			});

			$(".chapter > img").on("click", function (e) {
				const elm = $(this);
				const x = e.pageX - elm.offset().left;

				const findActive = chapter.find("img[style='display: block;']");
				if (x < elm.width() / 2) {
					const prev = findActive.prev();
					if (prev.length) {
						window.location.hash = prev.attr("id");
					}
				} else {
					const next = findActive.next();
					if (next.length) {
						window.location.hash = next.attr("id");
					}
				}
			})
			break;
	}

	$("#bookmark").on("click", async function () {
		const endpoint = window.location.pathname;
		const type = $(this).attr("type");

		// loading
		Swal.fire({
			title: 'Loading...',
			allowOutsideClick: false,
			allowEscapeKey: false,
			allowEnterKey: false,
			showConfirmButton: false,
			didOpen: () => {
				Swal.showLoading();
			},
		});

		const bookmarks = db.getItem("bookmarks") || '[]';
		switch (type) {
			case "add":
				const getData = await $.getJSON(`/api${endpoint}`);
				getData.endpoint = endpoint;

				const isAlready = JSON.parse(bookmarks).find(a => a.endpoint === endpoint);
				if (isAlready) return Swal.fire({
					icon: "error",
					title: "Already Bookmarked",
					text: "You already bookmarked this page",
					didOpen: (e) => {
						$(e).find(".swal2-confirm.swal2-styled").removeClass("swal2-styled").toggleClass("button");
					}
				});

				db.setItem("bookmarks", JSON.stringify([...JSON.parse(bookmarks), getData]));

				Swal.fire({
					title: "Bookmark",
					text: "Successfully bookmarked",
					icon: "success",
					didOpen: (e) => {
						$(e).find(".swal2-confirm.swal2-styled").removeClass("swal2-styled").toggleClass("button");
					}
				});

				$("#bookmark").text(" - Bookmark").attr("type", "remove");
				break;

			case "remove":
				var i;
				const newBookmarks = JSON.parse(bookmarks).filter(a => a.endpoint !== endpoint);
				db.setItem("bookmarks", JSON.stringify(newBookmarks));

				Swal.fire({
					title: "Bookmark",
					text: "Successfully removed",
					icon: "success",
					timer: 2000,
					timerProgressBar: true,
					didOpen: (e) => {
						Swal.showLoading();
						const b = Swal.getHtmlContainer().querySelector("b");
						timerInterval = setInterval(() => {
							b.textContent = Swal.getTimerLeft();
						}, 100);
					},
					willClose: () => {
						clearInterval(i);
					}
				});
				$("#bookmark").text(" + Bookmark").attr("type", "add");

				break;
		}
	})
}); 