$(window).scroll(function(){
    let scroll = $(window).scrollTop();
    document.getElementById("myBody").style.marginTop = (-100 - 0.5*scroll) + "px";
});