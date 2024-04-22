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



});