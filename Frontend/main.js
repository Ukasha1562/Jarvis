$(document).ready(function () {
// main text animation
  $('.text').textillate({
    loop: true,
    sync: true,
    in:{
      effect:"bounceIn",
    },
    out:{
      effect:"bounceOut",
    },
  });

// wave animation
  var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    style: "ios9",
    speed: 0.30,
    autostart: true
  });

// prompt animation
  $('.prompt').textillate({
    loop: true,
    sync: true,
    in:{
      effect:"fadeInUp",
      sync: true
    },
    out:{
      effect:"fadeOutUp",
      sync: true
    },
  });

  // Mic click
  $('#mic').click(function () { 
    eel.start_sound()
    $('#shape').attr('hidden', true);
    $('#wave').attr('hidden', false);
    eel.speak_converter()
  });



});