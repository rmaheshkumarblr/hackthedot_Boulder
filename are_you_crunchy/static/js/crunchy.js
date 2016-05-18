$(function(){
  $('#isCrunchyBtn').click(function(){
    var twUserId = $('#twUserId').val();
    var url = "/gettweets/" + twUserId;
    $.getJSON(url).done(function(data){
      var crunchiness = data.crunchy;
      $('#score').html(crunchiness);
      $('h4').show();
      if(crunchiness >= 10) {
        $('#isCrunchy').html('CONGRATULATIONS!!! YOU ARE CRUNCHY!!!');
        $('#score').addClass('crunchy');
      } else {
        $('#isCrunchy').html('You are not so Crunchy :(');
        $('#score').addClass('notcrunchy');
      }
    });
  });
});
