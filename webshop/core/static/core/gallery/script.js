
(function(b){function w(a){b(a.target).closest(".mbr-slider").hasClass("in")&&a.target.playVideo()}function p(a){a=b(a.target);"undefined"!==typeof b.fn.masonry&&a.outerFind(".mbr-gallery").each(function(){var c=b(this).find(".mbr-gallery-row").masonry({itemSelector:".mbr-gallery-item:not(.mbr-gallery-item__hided)",percentPosition:!0,horizontalOrder:!0});c.masonry("reloadItems");c.on("filter",function(){c.masonry("reloadItems");c.masonry("layout");b(window).trigger("update.parallax")}.bind(this,c));
c.imagesLoaded().progress(function(){c.masonry("layout")})})}function q(a,c,b,d,f){var g=a.find("img"),k=g[0].naturalWidth,m=g[0].naturalHeight;b=b/c>k/m?(c-2*f)*k/m:b-2*f;b=b>=k?k:b;c=(c-b*m/k)/2;g.css({width:parseInt(b),height:b*m/k});a.css("top",c+d)}function x(a,c,e,d,f,g){a.find(".modal-dialog .carousel-item").each(function(){if(!g&&!b(this)[0].classList.contains("carousel-item-next")&&!b(this)[0].classList.contains("carousel-item-prev")||g&&!b(this)[0].classList.contains("active"))b(this)[0].classList.contains("video-container")?
b(this).css({top:d,height:e-2*d-2*f}):q(b(this),e,c,d,f)})}function r(){var a=b(window).width()-0,c=b(window).height()-0,e=b(".mbr-gallery .modal");e.length&&n&&e.each(function(){var d,e=!1;b(this).find(".modal-dialog .carousel-item.carousel-item-next, .modal-dialog .carousel-item.carousel-item-prev").length?d=b(this).find(".modal-dialog .carousel-item.carousel-item-next, .modal-dialog .carousel-item.carousel-item-prev"):(d=b(this).find(".modal-dialog .carousel-item.active"),e=!0);d[0].classList.contains("video-container")?
d.css({top:0,height:c-0-20}):q(d,c,a,0,10);clearTimeout(t);t=setTimeout(x,200,b(this),a,c,0,10,e)})}if(!b("html").hasClass("is-builder")){var h=document.createElement("script");h.src="https://www.youtube.com/iframe_api";var u=document.getElementsByTagName("script")[0];u.parentNode.insertBefore(h,u);var l=[];b(".carousel-item.video-container img").css("display","none");window.onYouTubeIframeAPIReady=function(){var a=a||{};a.YTAPIReady||(a.YTAPIReady=!0,jQuery(document).trigger("YTAPIReady"));b(".video-slide").each(function(c){b(".video-container").eq(c).append('<div id ="mbr-video-'+
c+'" class="mbr-background-video" data-video-num="'+c+'"></div>').append('<div class="item-overlay"></div>');b(this).attr("data-video-num",c);if(-1!==b(this).attr("data-video-url").indexOf("vimeo.com")){var a={id:b(this).attr("data-video-url"),width:"100%",height:"100%",loop:!0};c=new Vimeo.Player("mbr-video-"+c,a);c.playVideo=Vimeo.play}else{var a=YT.Player,d;d=b(this).attr("data-video-url");d="false"===d?!1:(d=/(?:\?v=|\/embed\/|\.be\/)([-a-z0-9_]+)/i.exec(d)||/^([-a-z0-9_]+)$/i.exec(d))?d[1]:!1;
c=new a("mbr-video-"+c,{height:"100%",width:"100%",videoId:d,events:{onReady:w},playerVars:{rel:0}})}l.push(c)})}}b(document).on("add.cards",function(a){var c=b(a.target);c.find(".mbr-gallery-filter-all");c.on("click",".mbr-gallery-filter li > .btn",function(a){a.preventDefault();var d=b(this).closest("li");d.parent().find("a").removeClass("active");b(this).addClass("active");var f=d.closest("section").find(".mbr-gallery-row"),g=b(this).html().trim();c.find(".mbr-gallery-item").each(function(a,c){var e=
b(this),f=e.attr("data-tags").split(",").map(function(a){return a.trim()});-1!==b.inArray(g,f)||d.hasClass("mbr-gallery-filter-all")?e.removeClass("mbr-gallery-item__hided"):(e.addClass("mbr-gallery-item__hided"),setTimeout(function(){e.css("left","300px")},200))});setTimeout(function(){f.closest(".mbr-gallery-row").trigger("filter")},50)})});b(document).on("add.cards changeParameter.cards changeButtonColor.cards",function(a){var c=b(a.target),e=c.find(".mbr-gallery-filter-all"),d=[];c.find(".mbr-gallery-item").each(function(a){(b(this).attr("data-tags")||
"").trim().split(",").map(function(a){a=a.trim();-1===b.inArray(a,d)&&d.push(a)})});if(0<c.find(".mbr-gallery-filter").length&&b(a.target).find(".mbr-gallery-filter").hasClass("gallery-filter-active")&&!b(a.target).find(".mbr-gallery-filter").hasClass("mbr-shop-filter")){var f="",g=e.find("a").attr("class")||"",g=g.replace(/(^|\s)active(\s|$)/," ").trim();c.find(".mbr-gallery-filter ul li:not(li:eq(0))").remove();d.map(function(a){f+='<li><a class="'+g+'" href>'+a+"</a></li>"});c.find(".mbr-gallery-filter ul").append(f)}else c.find(".mbr-gallery-item__hided").removeClass("mbr-gallery-item__hided"),
c.find(".mbr-gallery-row").trigger("filter");p(a)});b(document).on("change.cards",function(a){p(a)});b(".mbr-gallery-item").on("click","a",function(a){a.stopPropagation()});var v,t,n=!1,h=b(document).find(".mbr-gallery");h.on("show.bs.modal",function(a){clearTimeout(v);v=setTimeout(function(){var c=b(a.relatedTarget).parent().index(),c=b(a.target).find(".carousel-item").eq(c).find(".mbr-background-video");b(a.target).find(".carousel-item .mbr-background-video");0<c.length&&(c=l[+c.attr("data-video-num")],
c.playVideo?c.playVideo():c.play())},500);n=!0;r()});h.on("slide.bs.carousel",function(a){a=b(a.target).find(".carousel-item.active .mbr-background-video");0<a.length&&(a=l[+a.attr("data-video-num")],a.pauseVideo?a.pauseVideo():a.pause())});b(window).on("resize load",r);h.on("slid.bs.carousel",function(a){a=b(a.target).find(".carousel-item.active .mbr-background-video");0<a.length&&(a=l[+a.attr("data-video-num")],a.playVideo?a.playVideo():a.play())});h.on("hide.bs.modal",function(a){l.map(function(a,
b){a.pauseVideo?a.pauseVideo():a.pause()});n=!1})})(jQuery);