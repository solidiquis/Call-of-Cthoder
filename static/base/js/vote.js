$(document).ready(function(){
  $('.upvote').click(function(event){
    event.preventDefault();
    var this_ = $(this);
    var commentID = this_.attr('comment-id');
    var urlEndpoint = this_.attr('href');

    $.ajax({
      url: urlEndpoint,
      method: "GET",
      success: function(response){
        $(`span[data-id="${commentID}"]`).html(response['score'])
      },
    });
  });
});

$(document).ready(function(){
  $('.downvote').click(function(event){
    event.preventDefault();
    var this_ = $(this);
    var commentID = this_.attr('comment-id');
    var urlEndpoint = this_.attr('href');

    $.ajax({
      url: urlEndpoint,
      method: "GET",
      success: function(response){
        $(`span[data-id="${commentID}"]`).html(response['score'])
      },
    });
  });
});
