$(document).ready(function(){
  $('.subscribe-form').submit(function(e){
    e.preventDefault();
    var this_ = $(this);
    var urlEndpoint = this_.attr('action');
    var formData = this_.serialize();

    $.ajax({
      url: urlEndpoint,
      method: "POST",
      data: formData,
      success: function(response){
        $('#inputEmail').val('');
        $('.subscription-message').text(response['success_message']);
      },
    })
  })
})
