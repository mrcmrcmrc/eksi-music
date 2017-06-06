var musics = [];
var queue_ = [];
var current;
var shuffle = false;
var auto_play = false;
var player;
var back_ = false;
var c = 0;
var previous;
var loved_tracks = [];

jQuery(document).ready(function($) {
  $(".box > img").each(function(i, element){
    musics[i] = $(element).attr('id');
  });
  
  $('.info').each(function(){
    this.innerText = this.innerText.replace(/\w\S*/g, function(txt){return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();});
  });

/*   jQuery('.box > .info').hover(function () {
    $(this).prev().css({
      'opacity' : '1',
      'box-shadow' : '0px 0px 21px 6px #F6F6F6'
    });
  }, function() {
    $(this).prev().css({
      'opacity' : '0.427',
      'box-shadow' : 'none',
    });
  });*/

});




function onPlayerStateChange(event) {
  switch(event.data) {
    case YT.PlayerState.ENDED:
    $('#playPauseIcon').removeClass('glyphicon-pause');
    $('#playPauseIcon').addClass('glyphicon-play');
    if(shuffle && auto_play)
    {
      cal(musics[getIDFromShuffle()]);
      back_=false;
    }
    else if(auto_play) {
      if(back_ == true)
      {
        if(c==queue_.length)
        {

        }
        else {
          cal(queue_[c])
          c = c+1
        }
      }
      else if ((current + 1) == musics.length)
        cal(musics[0]);
      else cal(musics[current + 1]);
    }
    break;

    case YT.PlayerState.PLAYING:
    $('#playPauseIcon').removeClass('glyphicon-play');
    $('#playPauseIcon').addClass('glyphicon-pause');
    break;

    case YT.PlayerState.PAUSED:
    $('#playPauseIcon').removeClass('glyphicon-pause');
    $('#playPauseIcon').addClass('glyphicon-play');
    break;

    case YT.PlayerState.BUFFERING:
    break;

    case YT.PlayerState.CUED:
    break;
  }
}


function onPlayerReady(event) {
  $('#playPauseIcon').removeClass('glyphicon-play');
  $('#playPauseIcon').addClass('glyphicon-pause');  
  //event.target.setVolume(100);
 // event.target.playVideo();
 }


jQuery(document).ready(function($) {
  jQuery('.box > img').click(function () {
    previous = current;
    var vidId = $(this).attr('id');
    current = musics.indexOf(vidId);
    queue_.push(vidId);
    currentShadow(vidId, musics[previous]);
    ToggleLoveIcon();
    SetGoToCurrent();
    $('#player').html('<iframe id="player_'+vidId+'" width="420" height="315" src="http://www.youtube.com/embed/' + vidId + '?enablejsapi=1&autoplay=1&autohide=1&showinfo=0" frameborder="0" allowfullscreen=0></iframe>');

    player = new YT.Player('player_'+vidId, {
    events: {
      'onStateChange': onPlayerStateChange,
      'onReady': onPlayerReady
      }
    });
  });
});


function cal(mID) {
    previous = current;
    var vidId = mID;
    current = musics.indexOf(vidId);
    if(back_ == false)
      queue_.push(vidId);
    
    currentShadow(vidId, musics[previous]);
    ToggleLoveIcon();
    SetGoToCurrent();
    $('#player').html('<iframe id="player_'+ mID +'" width="420" height="315" src="http://www.youtube.com/embed/' + mID + '?enablejsapi=1&autoplay=1&autohide=1&showinfo=0" frameborder="0" allowfullscreen=0></iframe>');

    player = new YT.Player('player_'+mID, {
    events: {
      'onStateChange': onPlayerStateChange,
      'onReady': onPlayerReady
      }
    });
}


 function ToggleVideo() {
  if(player.getPlayerState() === 1) {
    player.pauseVideo();
  }

  else if (player.getPlayerState() === 2)
    player.playVideo();

}


function StopVideo() {
  try {
    player.stopVideo();
    $('#playPauseIcon').removeClass('glyphicon-pause');
    $('#playPauseIcon').addClass('glyphicon-play');
  }
  catch (err) {
    console.log(err.message);
  }
}


function ToggleShuffle() {
  if (shuffle) {
    shuffle = false;
    $('#shuffle').css({
    color: 'rgb(21,21,21)'
  });
  }
  else {
    shuffle = true;
    $('#shuffle').css({
    color: 'darkred',
  });
  }
}


function ToggleAutoPlay() {
  if (auto_play) {
    auto_play = false;
    $('#autoplay').css({
      color : 'rgb(21,21,21)'
    });
  }
  else {
    auto_play = true;
    $('#autoplay').css({
      color : 'darkred'
    });
  }
  
}


function StepForward() {

  if(back_ == true && shuffle == false)
  {
    if(c == queue_.length)
    {
      back_=false;
      if(auto_play)
      {
        if ((current + 1) == musics.length)
        {
          cal(musics[0]);
        }
       else
       {
        cal(musics[current + 1]);
      }
    }
  }
    else
    {
      cal(queue_[c]);
      c = c+1;
    }
  }
  else if (auto_play)
   {
    if(shuffle)
    {
    back_ = false;
    cal(musics[getIDFromShuffle()]);
    }

  else {

    if ((current + 1) == musics.length)
      cal(musics[0]);
    else
      cal(musics[current + 1]);
  }
}
}

function StepBackward() {
  if(back_ == false)
  {
    c = queue_.length;
        back_ = true;
  }
  if(c == 1) {
    //listede başa geldi daha fazla geri gidemez
  }
  else {
    cal(queue_[c-2]);
    c = c-1;

  }
}

function getIDFromShuffle() {
  var r  = current;
  while (r == current)
    var r = Math.floor(Math.random() * musics.length);
  return r;
}

function currentShadow(c, p) {
  $('#' + c).parent('.box').css({
    'box-shadow': '0px 0px 30px 8px darkred',
    'opacity' : '1'
    });

  $('#' + p).parent('.box').css({
    'box-shadow': '',
    'opacity' : '0.427'
    });
}

function Love() {
  if ($.inArray(musics[current], loved_tracks) == -1) {
    loved_tracks.push(musics[current]);
    ToggleLoveIcon();
  }
  else {
    unLove(musics[current]);
  }
}

function unLove(trackID) {
  var i = loved_tracks.indexOf(trackID);
  loved_tracks.splice(i,1);
  ToggleLoveIcon();

}

function ToggleLoveIcon () {
  if($.inArray(musics[current], loved_tracks) == -1) {
      $("#heart").css({
      'color':'rgb(21,21,21)'
    });
  }
  else $("#heart").css({
      'color':'red'
    }); 
  
}

function ShowLovedTracks() {

}

function SetGoToCurrent() {
  $('#goToCurrent').attr('href','#' + musics[current]);
}

