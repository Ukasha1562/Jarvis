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

// wave initilizer
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
    eel.AllPrompts()
  });


  // hot-word key press
  function hot_key(e){
    if (e.key=='j' && e.metaKey){
      eel.start_sound()
      $('#shape').attr('hidden', true);
      $('#wave').attr('hidden', false);
      eel.AllPrompts()
    }
  }
  document.addEventListener('keyup',hot_key,false)


  // for chatting with text
  function text_input(message){
    if (message!=""){
      $('#shape').attr('hidden', true);
      $('#wave').attr('hidden', false);
      eel.AllPrompts(message);
      $("#chatbox").val("")
      $('#mic').attr('hidden', false);
      $('#send').attr('hidden', true);
    }
  }


  // for showing or hiding send button
  function send_button(message){
    if(message.length==0){
      $('#mic').attr('hidden', false);
      $('#send').attr('hidden', true);
    }
    else{
      $('#mic').attr('hidden', true);
      $('#send').attr('hidden', false);
    }
  }


  // for showing and hiding mic button and send button after clicking chatbox
  $('#chatbox').keyup(function () {
    let message=$('#chatbox').val();
    send_button(message) 
  });


  // for functions after clicking send button
  $('#send').click(function () { 
    let message=$('#chatbox').val();
    text_input(message)
  });


  // for same like above functions but with enter key
  $('#chatbox').keypress(function (e) {
    key=e.which;
    if(key==13){
      let message=$('#chatbox').val();
      text_input(message)
    }
  });


});