// // Javascript function for Datawrapper Embed

function datawrapper(){
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