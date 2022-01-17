//NAVIGATION  
//When the user scrolls the page, execute myFunction
window.onscroll = function() {myFunction()};

// Get the navbar
var navbar = document.getElementById('navbar');

// Get the offset position of the navbar
var sticky = navbar.offsetTop;

// Add the sticky class to the navbar when you reach its scroll position. Remove "sticky" when you leave the scroll position
function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}




function(){
	"use strict";window.addEventListener("message",(function(e){
		if(void 0!==e.data["datawrapper-height"]){
			var t=document.querySelectorAll("iframe");
				for(var a in e.data["datawrapper-height"])
				for(var r=0;r<t.length;r++){
					if(t[r].contentWindow===e.source)t[r].style.height=e.data["datawrapper-height"][a]+"px"
				}
		}
	}
	)
	)
}
();




