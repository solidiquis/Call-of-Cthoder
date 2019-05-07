function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
};

// Confirms if user wants to delete comment.
$(document).ready(function(){
  $('.delete_comment').click(function(e){
    e.preventDefault();
    var this_ = $(this);
    var commentID = this_.attr('comment-id')

    $(`.confirm-delete[comment-id="${commentID}"]`).css('display', '');
    this_.css('display', 'none');
  })
})

// User chooses 'no': Gets rid of warning message and redisplays delete button.
$(document).ready(function(){
  $('.confirm-delete-no').click(function(e){
    e.preventDefault();
    var this_ = $(this);
    var commentID = this_.attr('comment-id');

    $(`.delete_comment[comment-id="${commentID}"]`).css('display', '');
    $(`.confirm-delete[comment-id="${commentID}"]`).css('display', 'none');
  })
})

$(document).ready(function(){
  $('.confirm-delete-yes').click(function(e){
    e.preventDefault();
    var this_ = $(this);
    var commentID = this_.attr('comment-id');
    var urlEndpoint = this_.attr('href');
    var csrftoken = getCookie('csrftoken');

    $.ajax({
      url: urlEndpoint,
      method: 'POST',
      data: {'csrfmiddlewaretoken': csrftoken},
      success: function(response){
        $('.comments-section').html(response['comments'])},
    })
  })
})
