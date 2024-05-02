$(document).ready(function () {
  
  // Display prompt above the wave 
  eel.expose(DisplayMessage)
  function DisplayMessage(message){
    $(".prompt li:first").text(message);
    $('.prompt').textillate('start');
  }

  // Hide wave after prompt
  eel.expose(ShowShape)
  function ShowShape(){
    $("#shape").attr("hidden",false);
    $("#wave").attr("hidden",true);
  }

  // for sender history
  eel.expose(sender)
  function sender(message) {
    var chatbox= document.getElementById("chat-canvas-body")
    if (message.trim()!=""){
      chatbox.innerHTML+= `<div class="row justify-content-end mb-4">
      <div class="width-size">
      <div class="sender_message">${message}</div>
      </div>`;

      chatbox.scrollTop= chatbox.scrollHeight;
    }
  }

  // for receiver history
  eel.expose(receiver)
  function receiver(message) {
    var chatbox= document.getElementById("chat-canvas-body")
    if (message.trim()!=""){
      chatbox.innerHTML+= `<div class="row justify-content-start mb-4">
      <div class="width-size">
      <div class="receiver_message">${message}</div>
      </div>`;

      chatbox.scrollTop= chatbox.scrollHeight;
    }
  }

});