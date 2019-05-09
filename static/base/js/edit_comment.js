// Renders edit form with original content loaded into the text area.
$(document).ready(function(){
  $('.edit_comment').click(function(e){
    e.preventDefault();
    var this_ = $(this);
    var commentID = this_.attr('comment-id');
    var originalContent = $(`.reply-body[comment-id="${commentID}"]`).text().trim()
    var textArea = $(`[name="edit_body"][reply-id="${commentID}"]`)
    var form = $(`.edit-reply-secondary-form[reply-id="${commentID}"]`);
    var replyForms = $('.reply-secondary-form');
    var editForms = $('.edit-reply-secondary-form');

    // Closes the reply forms. Don't want edit and reply forms showing together.
    for (let replyForm of replyForms){
      replyForm.style.display = 'none'
    };

    textArea.val(originalContent);
    form.css('display', 'flex');
  })
});

// Logic for the cancel button that closes edit comment form.
$(document).ready(function(){
  $('.cancel-edit').click(function(e){
    var this_ = $(this);
    var commentID = this_.attr('reply-id');
    $(`.edit-reply-secondary-form[reply-id="${commentID}"]`).css('display', 'none');
  })
});

// Logic for submitting edited-comment via AJAX call; re-renders comment section.
$(document).ready(function(){
  $('.edit-reply-secondary-form').submit(function(e){
    e.preventDefault();

    var this_ = $(this);
    var formData = this_.serialize()
    var urlEndpoint = this_.attr('action');

    $.ajax({
      url: urlEndpoint,
      method: 'POST',
      data: formData,
      success: function(response){
        $('.comments-section').html(response['comments'])
      },
    })
  })
});

$(document).ready(function(){
  $('.edit-parent').click(function(e){
    e.preventDefault();
    var this_ = $(this);
    var commentID = this_.attr('comment-id');
    var origContent = $(`.comment-body[comment-id="${commentID}"]`).html()
    var form = $(`.edit-parent-form[comment-id="${commentID}"]`); // Form tag
    var textArea = (`.parent-edit-ckeditor[comment-id="${commentID}"]`);

    var editor_config = {
          'skin': 'moono-lisa',
          'toolbar': 'Custom',
          'toolbar_Custom': [
              ['Styles'],
              ['Bold', 'Italic', 'Underline'],
              ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-',
              'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
              ],
          'height': 200,
          'width': 1110,
      };

    // Closes all other open editing forms.
    for (let editForm of $('.edit-parent-form')){
      editForm.style.display = 'none'
    };

    // Closes all other open reply forms.
    for (let replyForm of $('.reply-form')){
      replyForm.style.display = 'none'
    };

    // Renders ckeditor under the appropriate comment with matching IDs.
    CKEDITOR.replace(commentID, editor_config);
    CKEDITOR.instances[commentID].setData(origContent);
    form.css('display', 'flex');
  });

  // Cancel button logic which closes edit form
  $('.cancel-parent-edit').click(function(e){
    var this_ = $(this);
    var commentID = this_.attr('comment-id');
    var form = $(`.edit-parent-form[comment-id="${commentID}"]`);
    form.css('display', 'none');
  });


})
