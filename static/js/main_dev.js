/**
 * Created by Admin on 11/18/13.
 */
$( document ).ready(function() {
    $('#top-navigation ul').superfish();
    $( "#footer" ).load( "/site_regions/footers/", function( response, status, xhr ) {
      if ( status == "error" ) {
        var msg = "Sorry but there was an error: ";
        $( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
      }
      /*window.setTimeout("$('#video_main').attr('src',$('#video_main').attr('rel')+'?rnd='+(Math.random()*100000000)); $('#video_main')[0].play();",5000);*/
    });
     $( "#spotworkout" ).load( "/management/spotworkouts/", function( response, status, xhr ) {
      if ( status == "error" ) {
        var msg = "Sorry but there was an error: ";
        $( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
      }
    });
    $( "#featuredtrainers" ).load( "/management/featuredtrainers/", function( response, status, xhr ) {
      if ( status == "error" ) {
        var msg = "Sorry but there was an error: ";
        $( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
      }
    });

/*
    $("#jquery_jplayer_1").jPlayer({
		ready: function () {
			$(this).jPlayer("setMedia", {
				m4v: "http://www.jplayer.org/video/m4v/Big_Buck_Bunny_Trailer.m4v",
				ogv: "http://www.jplayer.org/video/ogv/Big_Buck_Bunny_Trailer.ogv",
				webmv: "http://www.jplayer.org/video/webm/Big_Buck_Bunny_Trailer.webm",
				poster: "http://www.jplayer.org/video/poster/Big_Buck_Bunny_Trailer_480x270.png"
			});
		},
		swfPath: "js",
		supplied: "webmv, ogv, m4v",
		size: {
			width: "640px",
			height: "360px",
			cssClass: "jp-video-360p"
		},
		smoothPlayBar: true,
		keyEnabled: true
	});
*/
    /*
    $( "#header" ).load( "/site_regions/headers/", function( response, status, xhr ) {
      if ( status == "error" ) {
        var msg = "Sorry but there was an error: ";
        $( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
      }
    });
    $( ".linkPopup").click(function (e) {
        e.preventDefault();
        console.log('link popup clicked');
        $( ".linkPopup").next().dialog({
          modal: true,
          buttons: {
            Ok: function() {
              $( this ).dialog( "close" );
            }
          }
        })
    });*/

});
function video_main(){
        $("#tokbox").hide();
        $('#video').show();
      window.setTimeout("$('#video_main').attr('src',$('#video_main').attr('rel')+'?rnd='+(Math.random()*100000000)); $('#video_main')[0].play();",5000);
}
function alltrainers(div_toload){
    var url = '/management/alltrainers/';
    $( "#" + div_toload ).load( url, function( response, status, xhr ) {
      if ( status == "error" ) {
        var msg = "Sorry but there was an error: ";
        $( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
      }
    });
}
function allWorkouts (){
    var url = '/management/allworkouts/';
    $( "#content-wrap" ).load( url, function( response, status, xhr ) {
      if ( status == "error" ) {
        var msg = "Sorry but there was an error: ";
        $( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
      }
    });
}
//management/trainer/{{ pUIitem.id }}/"
function trainer(obj){
    var url = '/management/trainer/' + obj + '/';
    $( "#content-wrap" ).load( url, function( response, status, xhr ) {
      if ( status == "error" ) {
        var msg = "Sorry but there was an error: ";
        $( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
      }
    });
}
function workout(obj){
    var url = '/management/workout/' + obj + '/';
    $( "#content-wrap" ).load( url, function( response, status, xhr ) {
      if ( status == "error" ) {
        var msg = "Sorry but there was an error: ";
        $( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
      }
    });
}
function trainer_session(obj){
    var url = '/management/session/' + obj + '/';
    $( "#content-wrap" ).load( url, function( response, status, xhr ) {

      if ( status == "error" ) {
        var msg = "Sorry but there was an error: ";
        $( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
      }
    });
}
function linkclick(obj){
    if ($('#video_main') && $('#video_main')[0]){
        $('#video_main')[0].pause();
        $('#video_main').src=null;
        if($('#video_main')[0])$('#video_main')[0].src=null;
    }
    //$('#video_main')[0].src=null;
    //$('#video_main').src=null;

    var url = '/site_regions/footer/' + obj + '/';
    $( "#content-wrap").hide();
    $( "#content-wrap" ).load( url, function( response, status, xhr ) {
      if ( status == "error" ) {
        var msg = "Sorry but there was an error: ";
        $( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
      } else {
          $( "#content-wrap").html($( "#content-wrap").text().replace("\"",""));
            $( "#content-wrap").show();
      }
    });
}
function featuredworkout(obj){
    var url = '/management/workouts/';// + obj + '/';
    $( "#content" ).load( url, function( response, status, xhr ) {
      if ( status == "error" ) {
        var msg = "Sorry but there was an error: ";
        $( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
      }
    });
}
function oneonone(obj){
    var url = '/management/trainers/';// + obj + '/';
    $( "#content" ).load( url, function( response, status, xhr ) {
      if ( status == "error" ) {
        var msg = "Sorry but there was an error: ";
        $( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
      }
    });
}
 function find(obj){
    var url = '/site_regions/footer/';// + obj + '/';
    $( "#content" ).load( url, function( response, status, xhr ) {
      if ( status == "error" ) {
        var msg = "Sorry but there was an error: ";
        $( "#error" ).html( msg + xhr.status + " " + xhr.statusText );
      }
    });
 }
/*
    if (!$( obj).attr('wndcrtd')) {
        $( obj).next().attr('id','wndcrtd_'+parseInt(Math.random()*10000));
        $( obj).attr('wndcrtd',$( obj).next().attr('id'));
        $( obj).next().dialog({
             open: function() {
                $('.ui-widget-overlay').addClass('custom-overlay');
            },
            close: function() {
                $('.ui-widget-overlay').removeClass('custom-overlay');
            },
          autoOpen: false,
          modal: true,
          buttons: {
            Ok: function() {
              $( this ).dialog( "close" );
            }
          }
        });
    }
    $('#'+$( obj).attr('wndcrtd')).dialog('open');
    return false;
}*/