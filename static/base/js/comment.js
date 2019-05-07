$(document).ready(function(){
  $('.comment-form').submit(function(e){
      e.preventDefault();
      for (var instance in CKEDITOR.instances){
        CKEDITOR.instances[instance].updateElement()
      };
      var thisForm = $(this);
      var formData = thisForm.serialize()
      var urlEndpoint = thisForm.attr('action')

	    $.ajax({
        url: urlEndpoint,
        method: "POST",
        data: formData,
        success: function(response){
            CKEDITOR.instances['id_body'].setData('')
            $('.comments-section').html(response['comments']);
        },
      })
    })
  })
